import logging

from PySide6.QtCore import QAbstractItemModel, Qt, Slot
from PySide6.QtGui import QFont, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QTableView

from models import StockModel


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
        self.raw_model = StockModel()
        self.setModel(self.raw_model)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    @Slot(bool)
    def handle_stock_added_signal(self):
        logging.debug("Handling Stock Added Signal")
        logging.debug("Updating the table view.")
        self.setModel(StockModel())
        self.viewport().update()

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
