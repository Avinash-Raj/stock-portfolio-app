import logging
from dataclasses import asdict
from typing import Any, Dict, List, Optional

from PySide6 import QtCore
from PySide6.QtCore import QModelIndex, Qt
from PySide6.QtSql import QSqlDatabase, QSqlRecord, QSqlTableModel

from stocks.entities import StockItem


class QSqlRecordWrapper(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.record = None


class StockModel(QSqlTableModel):
    beforeStockUpdate = QtCore.Signal(int, QSqlRecordWrapper)

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
            "Current Price",
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
        self.beforeStockUpdate.connect(self._before_update)

        # connect to beforeInsert signal
        self.beforeInsert.connect(self._before_insert)

    @QtCore.Slot(int, QSqlRecordWrapper)
    def _before_update(self, record_index: int, wrapper: QSqlRecordWrapper):
        """
        Slot which was triggered before record update
        """
        logging.debug("Before update slot gets called.")
        current_datetime = QtCore.QDateTime.currentDateTime().toUTC().toString(QtCore.Qt.DateFormat.ISODate)
        wrapper.record.setValue("dt_updated", current_datetime)

    def _before_insert(self, record: QSqlRecord):
        """
        Slot which was triggered before record insert.
        """
        logging.debug("Before insert slot gets called.")
        # turn symbol to upper case
        symbol = record.value("symbol").upper()
        record.setValue("symbol", symbol)

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

    def select_rows_by_ids(self, ids_to_select: List[int], reset_filter=True) -> List[int]:
        ids = ",".join([str(i) for i in ids_to_select])
        # Set the filter on the model to display only records with the specified IDs
        self.setFilter(f"id IN ({ids})")
        record_ids = []
        if self.select() and self.rowCount() > 0:
            for i in range(self.rowCount()):
                record_ids.append(i)
        if reset_filter:
            self.setFilter("")
        return record_ids

    def delete_rows_by_ids(self, ids_to_delete: List[int]):
        return self.deleteRows(self.select_rows_by_ids(ids_to_delete, reset_filter=False))

    def deleteRows(self, ids: List[int]) -> bool:
        for i in ids:
            self.removeRow(i)
        return self.submitAll()

    # list rows
    def listRows(self) -> List[Dict]:
        """_
        suppossed list all the rows.
        """
        # Get all records from the model
        records = []
        for row in range(self.rowCount()):
            record = {}
            for column in range(self.columnCount()):
                value = self.data(self.index(row, column))
                record[self.headerData(column, role=QtCore.Qt.ItemDataRole.EditRole)] = value
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

    def updateRowInTable(self, row, record):
        wrapper = QSqlRecordWrapper()
        wrapper.record = record
        self.beforeStockUpdate.emit(row, wrapper)
        return super().updateRowInTable(row, wrapper.record)

    def updateRows(self, data: Dict[int, Dict[str, Any]]) -> Dict[int, str]:
        # Update the records
        output: Dict[int, str] = {}
        keys = ",".join([str(i) for i in data.keys()])
        self.setFilter(f"id IN ({keys})")
        self.select()
        for record_id, update_data in data.items():
            # Find the index of the record to update
            for row in range(self.rowCount()):
                index = self.index(row, 0)  # Assumes ID is in the first column
                if index.data() == record_id:
                    logging.debug(f"Going to update record id {record_id}")
                    # get the record
                    record = self.record(row)
                    # Update the columns
                    for column_name, value in update_data.items():
                        record.setValue(column_name, value)

                    # Save the changes
                    status = self.updateRowInTable(row, record)
                    if status:
                        output[record_id] = ""
                    else:
                        output[record_id] = self.lastError().text()
                    break  # Exit the inner loop
        self.submitAll()
        # reset filter
        self.setFilter("")

        return output


class StockModelWithFooter(StockModel):
    """
    Used only for displaying data on portfolio table.
    """

    def rowCount(self, parent=QModelIndex()):
        # Add one extra row for the footer
        return super().rowCount(parent) + 1

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        column = index.column()

        if column in [10, 11] and role == Qt.ItemDataRole.DisplayRole:
            date_time = super().data(index, role)
            return date_time.replace("T", " ").replace("Z", "")

        return super().data(index, role)


class SettingsModel(QSqlTableModel):
    def __init__(self, db=None):
        if db:
            super().__init__(db=db)
        else:
            super().__init__()
        self.setTable("settings")  # Set the table name here
        self.select()

    def createOrUpdateRecord(self, data) -> bool:
        # Check if a record already exists
        if self.rowCount() > 0:
            return self.updateData(0, data)  # Update the first record

        return self.insertData(data)  # Insert a new record

    def selectFirstRecord(self) -> Optional[QSqlRecord]:
        # Select only the first record
        self.setFilter("")  # Clear any existing filter
        self.select()
        if self.rowCount() > 0:
            return self.record(0)  # Return the first record
        return None

    def insertData(self, data) -> bool:
        # Insert a new record with the provided data
        self.insertRow(self.rowCount())
        for column, value in data.items():
            column_id = self.fieldIndex(column)
            self.setData(self.index(self.rowCount() - 1, column_id), value, Qt.ItemDataRole.EditRole)

        # Submit the changes to the database
        return self.submitAll()

    def updateData(self, row, data) -> bool:
        # Update the specified row with the provided data
        print(f"Gonna update {row}")
        record: Optional[QSqlRecord] = self.selectFirstRecord()
        if not record:
            return False
        for column, value in data.items():
            column_id = self.fieldIndex(column)
            record.setValue(column_id, value)
        self.updateRowInTable(row, record)
        # Submit the changes to the database
        return self.submitAll()
