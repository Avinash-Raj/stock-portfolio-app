from dataclasses import dataclass
from typing import Optional, Tuple

from actions import SpinnerBase
from models import DB_NAME, StockModelController
from widgets.spinner import SpinningThread, spinning


@dataclass
class AddStockAction(SpinnerBase):
    @spinning(db_name=DB_NAME)
    def perform(self, *args, thread: Optional[SpinningThread] = None, **kwargs) -> Tuple[bool, str]:
        controller = StockModelController(thread.db if thread else None)
        return controller.add_stock_item(*args, **kwargs), thread.db.lastError().text()


@dataclass
class RefreshStockAction(SpinnerBase):
    @spinning(db_name=DB_NAME)
    def perform(self, thread: Optional[SpinningThread] = None) -> Tuple[bool, str]:
        controller = StockModelController(thread.db)
        return controller.refresh_stocks()
