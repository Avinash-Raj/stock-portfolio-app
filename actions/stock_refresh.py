from dataclasses import dataclass
from typing import Tuple

from actions import SpinnerBase
from models import DB_NAME, StockModelController
from views.spinner import spinning


@dataclass
class RefreshStock(SpinnerBase):
    @spinning(callback=None, db_name=DB_NAME)
    def refresh(self, thread=None) -> Tuple[bool, str]:
        controller = StockModelController(thread.db if thread else None)
        return controller.refresh_stocks()
