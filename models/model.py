import logging
from dataclasses import asdict
from typing import Any, List, Optional

from PySide6 import QtCore
from PySide6.QtSql import QSqlDatabase, QSqlRecord, QSqlTableModel

from entities import StockItem


class StockModel(QSqlTableModel):
    def __init__(self, db: Optional[QSqlDatabase] = None):
        if db:
            super().__init__(db=db)
        else:
            super().__init__()

        # Set the table name
        self.setTable("stocks")
        self.select()
        self._header = [
            "ID",
            "Name",
            "Price",
            "Shares",
            "Cost Basis",
            "Market Value",
            "Gain",
            "Symbol",
            "Price Paid",
            "Currency",
            "Created At",
            "Updated At",
        ]

        # connect to beforeUpdate signal
        self.beforeUpdate.connect(self._before_update)

        # connect to beforeInsert signal
        self.beforeInsert.connect(self._before_insert)

    def _before_update(self, record_index: int, record: QSqlRecord):
        """
        Slot which was triggered before record update
        """
        logging.debug("Before update slot gets called.")
        record.setValue("dt_updated", "")

    def _before_insert(self, record: QSqlRecord):
        """
        Slot which was triggered before record insert.
        """
        logging.debug("Before insert slot gets called.")

    def headerData(
        self,
        section,
        orientation: QtCore.Qt.Orientation = QtCore.Qt.Orientation.Horizontal,
        role=QtCore.Qt.ItemDataRole.DisplayRole,
    ):
        if orientation == QtCore.Qt.Orientation.Horizontal:
            if role == QtCore.Qt.ItemDataRole.DisplayRole:
                return self._header[section]
            if role == QtCore.Qt.ItemDataRole.EditRole:
                return super().headerData(section, orientation, QtCore.Qt.ItemDataRole.DisplayRole)
        return super().headerData(section, orientation, role)

    # Custom function to add a new row to the table
    def addRow(self, data: StockItem) -> bool:
        logging.debug("Adding a new stock record...")
        row = self.rowCount()
        self.insertRows(row, 1)
        for col_name, value in asdict(data).items():
            self.setData(self.index(row, self.fieldIndex(col_name)), value, QtCore.Qt.ItemDataRole.EditRole)
        current_datetime = QtCore.QDateTime.currentDateTime().toUTC().toString(QtCore.Qt.DateFormat.ISODate)
        self.setData(self.index(row, self.fieldIndex("dt_created")), current_datetime, QtCore.Qt.ItemDataRole.EditRole)
        self.setData(self.index(row, self.fieldIndex("dt_updated")), current_datetime, QtCore.Qt.ItemDataRole.EditRole)
        return self.submitAll()

    # Custom function to delete a row from the table
    def deleteRow(self, index: int) -> bool:
        self.removeRow(index)
        return self.submitAll()

    # list rows
    def listRows(self) -> List[Any]:
        """_
        suppossed list all the rows.
        """
        # Get all records from the model
        records = []
        for row in range(self.rowCount()):
            record = {}
            for column in range(self.columnCount()):
                value = self.data(self.index(row, column))
                record[self.headerData(column)] = value
            records.append(record)
        return records

    def filterRows(self, value, by="symbol", count=1, reset_filter=True):
        """
        Filter records by specific column.

        Args:
            value (str): value to filter for
            by (str, optional): Column to filter on . Defaults to 'symbol'.
            count (int): how many rows to return
        """
        self.setFilter(f"{by}='{value}'")
        if self.select() and self.rowCount() > 0:
            for i in range(self.rowCount()):
                if i < count:
                    yield self.record(i)
        if reset_filter:
            self.setFilter("")

    def updateRow(self, row_index: int, record: QSqlRecord):
        """
        Update a record based on the record's primary key ID.
        """
        # call updateRowInTable to update the row in the model
        self.updateRowInTable(row_index, record)
        # call submitAll to submit the changes to the database
        return self.submitAll()
