from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QTableView,
    QGraphicsOpacityEffect,
    QGraphicsDropShadowEffect,
    QHeaderView,
)
from PySide6.QtCore import (
    QPropertyAnimation,
    QEasingCurve,
    QParallelAnimationGroup,
    QSize,
    Qt,
)
from PySide6.QtGui import QColor
from windows.ui_interface import Ui_MainWindow
from slots.receivers import *
from models import DB, StockModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Set the window title
        self.setWindowTitle("My Stocks")
        self.setup()

    def setup(self):
        self.initiate_signals()
        self.setup_animation(self.ui.LeftMenuContainer)
        self.default_actions()

    def default_actions(self):
        """
        Default actions at the first place.
        """
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.LeftMenuContainer.hide()
        self.ui.stackedWidget.setCurrentWidget(self.ui.portfolio_page)
        # Create the model
        self.model = StockModel()
        column_ids_to_hide = [7, 8, 9]

        # Create the table view and set the model
        self.table_view = QTableView(self)
        self.table_view.setModel(self.model)
        for id in column_ids_to_hide:
            self.table_view.hideColumn(id)

        # replace the existing tablewidget with the table view
        self.ui.tableFrame.layout().replaceWidget(self.ui.tableWidget, self.table_view)
        # Set the last header to horizontally stretch to fill the remaining space
        header = self.table_view.horizontalHeader()
        header.setStretchLastSection(True)
        # header.setSectionResizeMode(QHeaderView.ResizeToContents)

    def setup_animation(self, widget: QWidget):
        """
        Sets the initial animation.
        """
        # Set up opacity effect
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.0)
        widget.setGraphicsEffect(self.opacity_effect)

        self.opacity_animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(250)
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)
        self.opacity_animation.setEasingCurve(QEasingCurve.OutQuad)

        # self.minimum_width_animation = QPropertyAnimation(self.ui.LeftMenuContainer, b"minimumwidth")
        # self.minimum_width_animation.setDuration(500)
        # self.minimum_width_animation.setEasingCurve(QEasingCurve.OutQuad)
        # create the shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setColor(QColor("white"))
        shadow.setOffset(0, 0)
        self.ui.topBarFrame.setGraphicsEffect(shadow)

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
        self.ui.addBtn.clicked.connect(lambda: open_add_stock_dialog(self))
