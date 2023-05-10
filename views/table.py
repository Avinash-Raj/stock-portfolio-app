import logging
from typing import List

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QAction, QContextMenuEvent, QFont, QStandardItem, QStandardItemModel
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QMenu, QTableView

from entities.classes import CURRENCIES
from models import StockModel, StockModelController
from settings import PORTFOLIO_TABLE_AMOUNT_COLUMN_NAMES, PORTFOLIO_TABLE_COLUMN_NAMES_TO_HIDE
from slots.receivers import refresh_stocks_slot
from themes.colors import TABLE_CELL_GREEN_BACKGROUND_COLOR, TABLE_CELL_RED_BACKGROUND_COLOR


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


class StockPortfolioTableView(BaseTableView):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.parent_widget = parent
        self.model_cls = StockModel
        self.setModel(self.model_cls())
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.initUI()

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
        refresh_stocks_slot(self.parent_widget, self.parent_widget.after_stock_refresh)

    @Slot()
    def on_delete_menu_triggered(self) -> None:
        selected_rows = self.get_selected_rows()
        column_id = 0  # first column, ie. ID
        record_ids = []
        for row_id in selected_rows:
            record_ids.append(self.get_cell_data(row_id, column_id))
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

    def _convert_to_standard_model(self, model: QSqlTableModel) -> QStandardItemModel:
        """
        Convert QAbstractItemModel to QStandardItemModel
        """
        standard_model = QStandardItemModel()
        standard_model.setColumnCount(model.columnCount())
        standard_model.setRowCount(model.rowCount())
        amount_column_indexes = [model.fieldIndex(i) for i in PORTFOLIO_TABLE_AMOUNT_COLUMN_NAMES]

        for i in range(model.columnCount()):
            # Set header data for QStandardItemModel
            header_item = QStandardItem(model.headerData(i, Qt.Orientation.Horizontal))
            standard_model.setHorizontalHeaderItem(i, header_item)
            is_amount_column = bool(i in amount_column_indexes)
            is_gain_column = i == model.fieldIndex("gain")

            for j in range(model.rowCount()):
                value = model.data(model.index(j, i))
                preceeding_text = ""
                if is_amount_column:
                    currency_code = model.data(model.index(j, model.fieldIndex("currency")))
                    currency_symbol = CURRENCIES[currency_code].symbol
                    preceeding_text = f"{currency_symbol} "
                value = f"{preceeding_text}{value}"
                item = QStandardItem()
                item.setData(value, Qt.ItemDataRole.DisplayRole)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                # set font for all amount columns
                if is_amount_column:
                    item.setFont(QFont("Arial", 12))
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
