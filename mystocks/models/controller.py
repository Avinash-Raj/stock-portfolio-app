import logging
from dataclasses import asdict
from typing import Any, Dict, List, Optional

from PySide6.QtSql import QSqlDatabase

from mystocks.entities import StockItem
from mystocks.models.model import SettingsModel, StockModel
from mystocks.models.model_utils import QSqlRecordToDict
from mystocks.utils.helpers import create_stock_item, update_stock_info


class StockModelController:
    """
    DB Stock Controller
    This class does the interaction with the Stock DB Model.
    """

    def __init__(self, db: Optional[QSqlDatabase] = None):
        self.model = StockModel(db)

    def select_rows_by_symbol(self, symbol):
        """
        Selects the db record by symbol.
        """
        rows = list(self.model.filterRows(symbol, reset_filter=False))
        if not rows:
            self.model.setFilter("")
            raise ValueError(f"Stock with the symbol {symbol} does not exists.")

        return rows

    def get_row_id_by_symbol(self, symbol):
        """
        Selects the db record and return it's corresponding row id.
        """
        rows = self.select_rows_by_symbol(symbol)
        row_id = None
        for i, row in enumerate(rows):
            if row.value("symbol") == symbol:
                row_id = i

        if row_id is None:
            raise ValueError(f"Stock with the symbol {symbol} does not exists.")

        return row_id

    def add_stock_item(self, symbol: str, price: float, quantity: int) -> bool:
        stock_item = create_stock_item(symbol, price, quantity)
        if not stock_item:
            logging.error(f'Failed to get stock information for "{symbol}"')
            return False
        logging.debug(f"Stock Item Info, {asdict(stock_item)}")
        return self.model.addRow(stock_item)

    def update_stock_item(self, symbol, column_values: dict) -> bool:
        row_id: int = self.get_row_id_by_symbol(symbol)
        record = self.model.record(row=row_id)
        for name, value in column_values.items():
            record.setValue(name, value)
        # clear filter
        self.model.setFilter("")
        return self.model.updateRowInTable(row_id, record)

    def remove_stock_item(self, symbol) -> bool:
        # filter the table by sumbol
        is_deleted = False
        row_id: int = self.get_row_id_by_symbol(symbol)
        self.model.deleteRow(row_id)
        # clear filter
        self.model.setFilter("")
        return is_deleted

    def remove_stocks(self, ids: List[int]) -> bool:
        result = self.model.delete_rows_by_ids(ids)
        self.model.setFilter("")
        return result

    # def update_stocks(self, )
    def refresh_stocks(self):
        """
        Helps to refresh all the stocks ie, update it's current_pricem cost_babis and gain.
        """
        out: Dict[int, Dict[str, Any]] = {}
        columns_to_update = ["price", "cost_basis", "market_value", "gain"]
        for row in self.model.listRows():
            row_id = row["id"]
            item = StockItem(**row)
            updated_item = update_stock_info(item)
            values_dict = {}
            for col in columns_to_update:
                values_dict[col] = getattr(updated_item, col)
            out[row_id] = values_dict
        status = True
        error = ""
        for row_id, err in self.model.updateRows(out).items():
            if err:
                status = False
                logging.debug(f"Failed to refresh stock id {row_id}, {err}")
                error += err
            else:
                logging.debug(f"Stock id {row_id} updated successfully.")
        return status, error


class SettingsModelController:
    """
    DB Settings Controller
    This class does the interaction with the Settings DB Model.
    """

    def __init__(self, db: Optional[QSqlDatabase] = None):
        self.model = SettingsModel(db)

    def add_or_update_setting(self, local_currency: str, columns_to_convert: str) -> bool:
        print(local_currency, columns_to_convert)
        data = {"local_currency": local_currency, "columns_to_convert": columns_to_convert}
        return self.model.createOrUpdateRecord(data=data)

    def get_settings(self) -> Dict[Any, Any]:
        record = self.model.selectFirstRecord()
        if not record:
            return {}
        return QSqlRecordToDict(record)
