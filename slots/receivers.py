from PySide6.QtCore import QPropertyAnimation

from actions.stock_refresh import RefreshStock
from themes.colors import *
from windows.add_stock import AddStockDialog


def on_open_menu_button_press(self):
    # print(self.ui.LeftMenuContainer.width(), self.ui.LeftMenuContainer.height())
    # print(self.ui.LeftMenuContainer.sizeHint())
    # default_size: QSize = self.ui.LeftMenuContainer.sizeHint()
    # default_size.setWidth(147, 357)
    # self.ui.LeftMenuContainer.resize(QSize(147, 357))
    self.opacity_animation.setDirection(QPropertyAnimation.Direction.Forward)
    self.ui.menuOpenBtn.hide()
    self.ui.LeftMenuContainer.show()
    # start open/close animation
    # self.minimum_width_animation.setDirection(QPropertyAnimation.Direction.Forward)
    # self.minimum_width_animation.setStartValue(0)
    # self.minimum_width_animation.setEndValue(147)
    # self.minimum_width_animation.start()

    # start opacity animation
    self.opacity_animation.start()


def on_close_menu_button_press(self):
    self.opacity_animation.setDirection(QPropertyAnimation.Direction.Backward)
    self.ui.menuOpenBtn.show()

    # self.minimum_width_animation.setDirection(QPropertyAnimation.Direction.Backward)
    # self.minimum_width_animation.setStartValue(147)
    # self.minimum_width_animation.setEndValue(0)
    self.opacity_animation.start()
    # self.minimum_width_animation.start()
    self.ui.LeftMenuContainer.hide()


def set_menu_button_colors(self, button):
    # Set the background color of the selected button to green
    button.setStyleSheet(f"QPushButton {{ background-color: {BUTTON_BG_COLOR} }}")

    # Set the background color of the other buttons to their default color
    for other_button in [self.ui.portfolioBtn, self.ui.settingsBtn, self.ui.helpBtn]:
        if other_button is not button:
            print(f"setting syte to none for {other_button}")
            other_button.setStyleSheet("")


def open_portfolio_page(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.portfolio_page)
    set_menu_button_colors(self, self.ui.portfolioBtn)


def open_help_page(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.help_page)
    set_menu_button_colors(self, self.ui.helpBtn)


def open_settings_page(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.setting_page)
    set_menu_button_colors(self, self.ui.settingsBtn)


def open_add_stock_dialog(self):
    dialog = AddStockDialog(self)
    dialog.stock_added_signal.connect(self.table_view.handle_stock_added_signal)
    dialog.exec()


def refresh_stocks(self):
    refresh_stock = RefreshStock(self, callback=self.after_stock_refresh)
    refresh_stock.refresh()
