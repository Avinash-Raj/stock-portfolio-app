from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, Slot
from PySide6.QtWidgets import QMainWindow, QWidget

from slots.receivers import (
    on_close_menu_button_press,
    on_open_menu_button_press,
    open_help_page,
    open_portfolio_page,
    open_settings_page,
    set_menu_button_colors,
)
from windows.add_stock import AddStockDialog
from windows.settings_page import SettingsPage
from windows.stock_page import StockPage
from windows.ui_interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Set the window title
        self.setWindowTitle("My Stocks")
        self.stock_page = StockPage(self)
        self.settings_page = SettingsPage(self)
        self.setup()

    def setup(self):
        self.initiate_signals()
        self.setup_animation(self.ui.LeftMenuContainer)
        self.default_actions()
        self.load_stock_page()

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
        # upon clicking cancel button on settings page
        self.ui.buttonBox.rejected.connect(lambda: open_portfolio_page(self))
        # reload table upon settings updation
        self.settings_page.settings_added_signal.connect(lambda: self.stock_page.table_view.reload_table())

    def setup_animation(self, widget: QWidget):
        """
        Sets the initial animation.
        """
        # Create the sidebar animation
        self.sidebar_animation = QPropertyAnimation(widget, b"maximumWidth", self)
        self.sidebar_animation.setDuration(500)
        self.sidebar_animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def default_actions(self):
        """
        Default actions at the first place.
        """
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.sidebar_width = 160
        self.sidebar_visible = False
        self.table_view = None
        on_close_menu_button_press(self)

    def load_stock_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.portfolio_page)
        # mark the portfolio button as selected by default
        set_menu_button_colors(self, self.ui.portfolioBtn)
        self.ui.refreshBtn.clicked.connect(self.stock_page.refresh_stocks_signal.emit)
        self.ui.addBtn.clicked.connect(self.open_add_stock_dialog)

    @Slot()
    def open_add_stock_dialog(self):
        """
        Open add stock dialog model and perform necessary actions.
        """
        dialog = AddStockDialog(self)
        dialog.stock_added_signal.connect(self.stock_page.table_view.handle_stock_added_signal)
        dialog.exec()
