import logging

from PySide6.QtCore import QEasingCurve, QParallelAnimationGroup, QPropertyAnimation, QSize, Qt, Slot
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QGraphicsDropShadowEffect,
    QGraphicsOpacityEffect,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from slots.receivers import *
from views.table import StockPortfolioTableView
from windows.add_stock import AddStockDialog
from windows.ui_interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Set the window title
        self.setWindowTitle("My Stocks")
        self.sidebar_width = 160
        self.setup()

    def setup(self):
        self.initiate_signals()
        self.setup_animation(self.ui.LeftMenuContainer)
        self.default_actions()

    def default_actions(self):
        """
        Default actions at the first place.
        """
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.sidebar_visible = False
        on_close_menu_button_press(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.portfolio_page)
        # mark the portfolio button as selected by default
        set_menu_button_colors(self, self.ui.portfolioBtn)

        # Create the table view and set the model
        self.table_view = StockPortfolioTableView(self)

        # replace the existing tablewidget with the table view
        self.ui.tableFrame.layout().replaceWidget(self.ui.tableWidget, self.table_view)
        # Set the last header to horizontally stretch to fill the remaining space
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setStretchLastSection(True)

    def setup_animation(self, widget: QWidget):
        """
        Sets the initial animation.
        """
        # Create the sidebar animation
        self.sidebar_animation = QPropertyAnimation(widget, b"maximumWidth", self)
        self.sidebar_animation.setDuration(500)
        self.sidebar_animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def initiate_signals(self):
        """
        Initiate signals.
        """
        self.ui.menuOpenBtn.clicked.connect(lambda: on_open_menu_button_press(self))
        self.ui.menuClose.clicked.connect(lambda: on_close_menu_button_press(self))
        # PAGES
        self.ui.portfolioBtn.clicked.connect(lambda: open_portfolio_page(self))
        self.ui.settingsBtn.clicked.connect(lambda: open_settings_page(self))
        self.ui.helpBtn.clicked.connect(lambda: open_help_page(self))
        self.ui.addBtn.clicked.connect(self.open_add_stock_dialog)
        self.ui.refreshBtn.clicked.connect(lambda: refresh_stocks_slot(self, self.after_stock_refresh))

    def after_stock_refresh(self, action_instance, status: bool, error: str):
        if status:
            logging.info("Stocks refreshed and table reloaded!")
            self.table_view.reload_table()

    @Slot()
    def open_add_stock_dialog(self):
        """
        Open add stock dialog model and perform necessary actions.
        """
        dialog = AddStockDialog(self)
        dialog.stock_added_signal.connect(self.table_view.handle_stock_added_signal)
        dialog.exec()
