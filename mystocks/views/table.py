import logging
from collections import defaultdict
from typing import Dict, List, Optional

from PySide6.QtCore import QRect, Qt, Slot
from PySide6.QtGui import QAction, QColor, QContextMenuEvent, QFont, QPalette, QPen, QStandardItem, QStandardItemModel
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QMenu, QStyledItemDelegate, QTableView

from mystocks.entities.classes import CURRENCIES, ConversionRate
from mystocks.models import SettingsModelController, StockModelController, StockModelWithFooter
from mystocks.settings import (
    PORTFOLIO_TABLE_AMOUNT_COLUMN_NAMES,
    PORTFOLIO_TABLE_COLUMN_NAMES_TO_HIDE,
    PORTFOLIO_TABLE_SUMUP_COLUMN_NAMES,
)
from mystocks.slots.receivers import refresh_stocks_slot
from mystocks.themes.colors import (
    TABLE_CELL_FORGEGROUND_COLOR,
    TABLE_CELL_FORGEGROUND_GREY_COLOR,
    TABLE_CELL_GREEN_BACKGROUND_COLOR,
    TABLE_CELL_RED_BACKGROUND_COLOR,
)


class BaseTableView(QTableView):
    """
    Base class for all the table views.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Set the font for the rows in the table
        row_font = QFont("Arial", 12)
        self.setFont(row_font)

    def horizontalHeader(self) -> QHeaderView:
        horizontal_header = super().horizontalHeader()
        # Set the font for the header of the table
        header_font = QFont("Arial", 13, QFont.Weight.Bold)
        horizontal_header.setFont(header_font)

        return horizontal_header


class BorderItemDelegate(QStyledItemDelegate):
    # def sizeHint(self, option, index):
    #     # Set the desired size for the cell
    #     return QSize(100, 200)  # Width: 100 pixels, Height: 50 pixels

    def paint(self, painter, option, index):
        # last row
        if index.row() == (index.model().rowCount() - 1) and index.column() in [4, 5, 6]:
            painter.save()

            # Add a border around sum columns
            border_rect: QRect = option.rect
            border_rect.setBottom(border_rect.bottom() - 1)
            border_rect.setRight(border_rect.right() - 1)
            painter.setPen(QPen(Qt.GlobalColor.magenta))
            painter.drawRect(border_rect)

            painter.restore()

        super().paint(painter, option, index)


class StockPortfolioTableView(BaseTableView):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.parent_widget = parent
        self.model_cls = StockModelWithFooter
        self.setModel(self.model_cls())
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.initUI()
        self.beautify()

    def beautify(self):
        """
        Beautifies the table.
        """
        self.setItemDelegate(BorderItemDelegate())
        # Set the desired row height
        row_height = 40  # Adjust this value to increase or decrease the row height
        for row in range(self.model().rowCount()):
            self.setRowHeight(row, row_height)

        self.setBackgroundRole(QPalette.ColorRole.Dark)
        self.setAutoFillBackground(True)

    def initUI(self):
        self.menu = QMenu(self)
        self.delete_menu = QAction("Delete", self)
        self.refresh_menu = QAction("Refresh", self)
        self.menu.addAction(self.delete_menu)
        self.menu.addAction(self.refresh_menu)
        self.delete_menu.triggered.connect(self.on_delete_menu_triggered)
        self.refresh_menu.triggered.connect(self.on_refresh_menu_triggered)

    def get_selected_rows(self) -> List[int]:
        selected_rows = list(set(index.row() for index in self.selectedIndexes()))
        return selected_rows

    def get_cell_data(self, row: int, col: int) -> str:
        index = self.model().index(row, col)
        return self.model().data(index)

    @Slot()
    def on_refresh_menu_triggered(self):
        refresh_stocks_slot(self.parent_widget, self.reload_table())

    @Slot()
    def on_delete_menu_triggered(self) -> None:
        selected_rows = self.get_selected_rows()
        column_id = 0  # first column, ie. ID
        record_ids = []
        for row_id in selected_rows:
            data = self.get_cell_data(row_id, column_id)
            if data:
                record_ids.append(data)
        if not record_ids:
            return None
        logging.info(f"Going to delete record ids, {record_ids}")
        controller = StockModelController()
        success = controller.remove_stocks(record_ids)
        # reload table on query success
        if success:
            logging.info(f"Record ids deleted successfullly!, {record_ids}")
            self.reload_table()
        return None

    @Slot(bool)
    def handle_stock_added_signal(self):
        logging.debug("Handling Stock Added Signal")
        logging.debug("Updating the table view.")
        self.reload_table()

    def reload_table(self):
        """
        Re-fetches the data from database.
        """
        self.setModel(self.model_cls())
        self.viewport().update()

    def contextMenuEvent(self, event: QContextMenuEvent):
        self.menu.exec(event.globalPos())

    @classmethod
    def get_standard_item(
        cls,
        value: str,
        alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter,
        font: QFont = QFont("Arial", 13, QFont.Weight.Bold),
        background: Optional[QColor] = None,
        foreground: Optional[QColor] = None,
    ) -> QStandardItem:
        item = QStandardItem()
        item.setData(value, Qt.ItemDataRole.DisplayRole)
        item.setTextAlignment(alignment)
        item.setFont(font)
        if background:
            item.setBackground(background)
        if foreground:
            item.setForeground(foreground)

        return item

    @classmethod
    def get_column_sum(cls, data_list: List) -> float:
        """
        returns the sum of all the rows on a particluar column.
        """
        return sum(data_list)

    def _convert_to_standard_model(self, model: QSqlTableModel) -> QStandardItemModel:
        """
        Convert QAbstractItemModel to QStandardItemModel
        """
        standard_model = QStandardItemModel()
        standard_model.setColumnCount(model.columnCount())
        standard_model.setRowCount(model.rowCount())
        amount_column_indexes = [model.fieldIndex(i) for i in PORTFOLIO_TABLE_AMOUNT_COLUMN_NAMES]
        sumup_column_indexes = [model.fieldIndex(i) for i in PORTFOLIO_TABLE_SUMUP_COLUMN_NAMES]
        row_count = model.rowCount()
        column_count = model.columnCount()
        data: Dict[int, list] = defaultdict(list)
        settings: Dict[str, str] = SettingsModelController().get_settings()
        local_currency, columns_to_convert = settings.get("local_currency", ""), settings.get("columns_to_convert", "")
        local_currency_symbol = ""
        conversion_rates: Dict[str, ConversionRate] = {}
        if local_currency:
            local_currency_symbol = CURRENCIES[local_currency].symbol

        for i in range(column_count):
            # Set header data for QStandardItemModel
            header_item = QStandardItem(model.headerData(i, Qt.Orientation.Horizontal))
            standard_model.setHorizontalHeaderItem(i, header_item)
            is_amount_column = bool(i in amount_column_indexes)
            is_gain_column = i == model.fieldIndex("gain")
            is_sumup_column_index = bool(i in sumup_column_indexes)
            column_name = model.headerData(i, Qt.Orientation.Horizontal, Qt.ItemDataRole.EditRole)

            for j in range(row_count):
                if j + 1 == row_count:
                    # last row (ie. Footer row)
                    item = self.get_standard_item("")
                    if i == model.fieldIndex("name"):
                        # name cell
                        cell_text = "Total"
                        item = self.get_standard_item(cell_text, font=QFont("Arial", 20, QFont.Weight.Bold))
                    elif is_sumup_column_index:
                        # column to sumup
                        cell_text = self.get_column_sum(data[i])
                        item = self.get_standard_item(
                            f"{local_currency_symbol if column_name in columns_to_convert else '$'} {cell_text:,.2f}",
                            font=QFont("Arial", 20, QFont.Weight.Bold),
                        )
                    # apply bg color for gain column
                    if is_gain_column:
                        gain_data = item.data(Qt.ItemDataRole.DisplayRole)
                        if "-" in gain_data:
                            item.setBackground(TABLE_CELL_RED_BACKGROUND_COLOR)
                        else:
                            item.setBackground(TABLE_CELL_GREEN_BACKGROUND_COLOR)
                        item.setForeground(TABLE_CELL_FORGEGROUND_COLOR)
                    standard_model.setItem(j, i, item)
                    continue
                value = model.data(model.index(j, i))

                preceeding_text = ""
                if is_amount_column:
                    currency_code = model.data(model.index(j, model.fieldIndex("currency")))

                    # check for existence of local currency
                    # if yes then convert appropriate column values to local currency
                    if local_currency and column_name in columns_to_convert and currency_code != local_currency:
                        # get or set conversion rate
                        currency_pair = f"{currency_code}_{local_currency}"
                        conversion_rate = conversion_rates.get(currency_pair)
                        if not conversion_rate:
                            conversion_rate = ConversionRate(currency_code, local_currency)
                            conversion_rates[currency_pair] = conversion_rate
                        # convert the value to local currency
                        converted_amount = conversion_rate.convert(value)

                        data[i].append(converted_amount)
                        # rounded upto 2 decimal places
                        value = f"{converted_amount:,.2f}"
                        preceeding_text = f"{local_currency_symbol} "
                    elif currency_code:
                        currency_symbol = CURRENCIES[currency_code].symbol
                        preceeding_text = f"{currency_symbol} "
                        data[i].append(value)
                        # round the value for display
                        value = f"{value:,.2f}"
                    else:
                        data[i].append(value)
                        # round the value for display
                        value = f"{value:,.2f}"
                else:
                    data[i].append(value)

                value = f"{preceeding_text}{value}"

                item = self.get_standard_item(value)
                # set font for all amount columns
                if is_amount_column:
                    item.setFont(QFont("Arial", 14, QFont.Weight.Bold))
                    item.setForeground(TABLE_CELL_FORGEGROUND_GREY_COLOR)
                # set background if in case of gain column
                if is_gain_column:
                    if "-" in value:
                        # loss
                        item.setBackground(TABLE_CELL_RED_BACKGROUND_COLOR)
                    else:
                        # gain
                        item.setBackground(TABLE_CELL_GREEN_BACKGROUND_COLOR)
                    item.setForeground(Qt.GlobalColor.black)
                standard_model.setItem(j, i, item)

        return standard_model

    def setModel(self, model: QSqlTableModel) -> None:
        super().setModel(self._convert_to_standard_model(model))
        self.column_ids_to_hide = [model.fieldIndex(i) for i in PORTFOLIO_TABLE_COLUMN_NAMES_TO_HIDE]
        for colid in self.column_ids_to_hide:
            self.hideColumn(colid)
