import logging
from typing import List

from PySide6.QtCore import QAbstractItemModel, Qt, Slot
from PySide6.QtGui import QAction, QContextMenuEvent, QFont, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QMenu, QTableView

from models import StockModel, StockModelController


class BaseTableView(QTableView):
    """
    Base class for all the table views.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Set the font for the rows in the table
        row_font = QFont("Tahoma", 12)
        self.setFont(row_font)

    def horizontalHeader(self) -> QHeaderView:
        horizontal_header = super().horizontalHeader()
        # Set the font for the header of the table
        header_font = QFont("Arial", 13, QFont.Weight.Bold)
        horizontal_header.setFont(header_font)

        return horizontal_header


class StockPortfolioTableView(BaseTableView):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.column_ids_to_hide = [7, 8, 9]
        self.model_cls = StockModel
        self.setModel(self.model_cls())
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.initUI()

    def initUI(self):
        self.menu = QMenu(self)
        self.delete_menu = QAction("Delete", self)
        self.menu.addAction(self.delete_menu)
        self.delete_menu.triggered.connect(self.on_delete_triggered)

    def get_selected_rows(self) -> List[int]:
        selected_rows = list(set(index.row() for index in self.selectedIndexes()))
        return selected_rows

    def get_cell_data(self, row: int, col: int) -> str:
        index = self.model().index(row, col)
        return self.model().data(index)

    @Slot()
    def on_delete_triggered(self) -> None:
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

    def _convert_to_standard_model(self, model: QAbstractItemModel) -> QStandardItemModel:
        """
        Convert QAbstractItemModel to QStandardItemModel
        """
        standard_model = QStandardItemModel()
        standard_model.setColumnCount(model.columnCount())
        standard_model.setRowCount(model.rowCount())

        for i in range(model.columnCount()):
            # Set header data for QStandardItemModel
            header_item = QStandardItem(model.headerData(i, Qt.Orientation.Horizontal))
            standard_model.setHorizontalHeaderItem(i, header_item)

            for j in range(model.rowCount()):
                item = QStandardItem()
                value = model.data(model.index(j, i))
                item.setData(value, Qt.ItemDataRole.DisplayRole)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                standard_model.setItem(j, i, item)

        return standard_model

    def setModel(self, model: QAbstractItemModel) -> None:
        super().setModel(self._convert_to_standard_model(model))
        for colid in self.column_ids_to_hide:
            self.hideColumn(colid)
