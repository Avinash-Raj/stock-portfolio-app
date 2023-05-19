from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QHeaderView

from stocks.slots.receivers import refresh_stocks_slot
from stocks.views.table import StockPortfolioTableView

if TYPE_CHECKING:
    from stocks.windows.main import MainWindow


class StockPage(QObject):
    refresh_stocks_signal = Signal()

    def __init__(self, main_window: MainWindow) -> None:
        super().__init__()
        self.main_window = main_window
        self.setup_table()

    def setup_table(self):
        """
        Setup the portfolio table.
        """
        # Create the table view and set the model
        table_view = StockPortfolioTableView(self.main_window)
        # Set the last header to horizontally stretch to fill the remaining space
        header = table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setStretchLastSection(True)

        self.table_view = table_view

        # replace the existing tablewidget with the table view
        self.main_window.ui.tableFrame.layout().replaceWidget(self.main_window.ui.tableWidget, self.table_view)
        self.refresh_stocks_signal.connect(lambda: refresh_stocks_slot(self.main_window, self.after_stock_refresh))

    def after_stock_refresh(self, action_instance, status: bool, error: str):
        if status:
            logging.info("Stocks refreshed and table reloaded!")
            self.table_view.reload_table()
