from typing import Callable

from PySide6.QtCore import QPropertyAnimation, Slot

from actions.stock_actions import AddStockAction, RefreshStockAction
from themes.colors import *


@Slot()
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


@Slot()
def on_close_menu_button_press(self):
    self.opacity_animation.setDirection(QPropertyAnimation.Direction.Backward)
    self.ui.menuOpenBtn.show()

    # self.minimum_width_animation.setDirection(QPropertyAnimation.Direction.Backward)
    # self.minimum_width_animation.setStartValue(147)
    # self.minimum_width_animation.setEndValue(0)
    self.opacity_animation.start()
    # self.minimum_width_animation.start()
    self.ui.LeftMenuContainer.hide()


@Slot()
def set_menu_button_colors(self, button):
    # Set the background color of the selected button to green
    button.setStyleSheet(f"QPushButton {{ background-color: {BUTTON_BG_COLOR} }}")

    # Set the background color of the other buttons to their default color
    for other_button in [self.ui.portfolioBtn, self.ui.settingsBtn, self.ui.helpBtn]:
        if other_button is not button:
            print(f"setting syte to none for {other_button}")
            other_button.setStyleSheet("")


@Slot()
def open_portfolio_page(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.portfolio_page)
    set_menu_button_colors(self, self.ui.portfolioBtn)


@Slot()
def open_help_page(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.help_page)
    set_menu_button_colors(self, self.ui.helpBtn)


@Slot()
def open_settings_page(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.setting_page)
    set_menu_button_colors(self, self.ui.settingsBtn)


@Slot(object, str, float, int, object)
def add_stock_slot(self, symbol, price, quantity, callback):
    action = AddStockAction(self, callback=callback)
    action.perform(symbol, price, quantity)


@Slot(object, object)
def refresh_stocks_slot(self, callback):
    action = RefreshStockAction(self, callback=callback)
    action.perform()
