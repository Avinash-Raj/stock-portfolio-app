import logging
import time
from dataclasses import dataclass
from typing import Tuple

from PySide6.QtCore import QThread, QTimer
from PySide6.QtWidgets import QWidget

from models import DB_NAME, StockModelController
from views.spinner import Spinner, SpinningWorker, spinning


@dataclass
class RefreshStock:
    parent: QWidget

    def __post_init__(self):
        self.spinner = Spinner(self.parent)

    @spinning(callback=None, db_name=DB_NAME)
    def refresh(self, thread=None) -> Tuple[bool, str]:
        controller = StockModelController(thread.db if thread else None)
        return controller.refresh_stocks(), ""
