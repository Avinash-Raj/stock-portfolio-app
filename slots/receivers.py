from PySide6.QtCore import Slot

from actions.stock_actions import AddStockAction, RefreshStockAction
from themes.colors import *


@Slot()
def on_open_menu_button_press(self):
    """
    Runs upon clicking sidebar open button.
    """

    start_width = 0
    end_width = self.sidebar_width
    self.sidebar_animation.setStartValue(start_width)
    self.sidebar_animation.setEndValue(end_width)
    self.sidebar_animation.start()
    self.sidebar_visible = True
    # hide menu
    self.ui.menuOpenBtn.hide()


@Slot()
def on_close_menu_button_press(self):
    """
    Runs upon clicking side bar close button.
    """
    start_width = self.sidebar_width
    end_width = 0
    self.sidebar_animation.setStartValue(start_width)
    self.sidebar_animation.setEndValue(end_width)
    self.sidebar_animation.start()

    self.sidebar_visible = False
    # hide menu
    self.ui.menuOpenBtn.show()


@Slot()
def set_menu_button_colors(self, button):
    # Set the background color of the selected button to green
    button.setStyleSheet(f"QPushButton {{ background-color: {BUTTON_BG_COLOR} }}")

    # Set the background color of the other buttons to their default color
    for other_button in [self.ui.portfolioBtn, self.ui.settingsBtn, self.ui.helpBtn]:
        if other_button is not button:
            # print(f"setting syte to none for {other_button}")
            other_button.setStyleSheet("")

    # if button == self.ui.portfolioBtn:
    #     # portfolio page selected
    #     frame = self.ui.portFolioBtnFrame
    #     frame.setStyleSheet("background-color: black;")  # Set the background color here


def show_or_hide_stock_buttons(self, show=True):
    """
    Show/hide stock buttons such as refresh button and stock add button.
    """
    if show:
        self.ui.refreshBtn.show()
        self.ui.addBtn.show()
    else:
        self.ui.refreshBtn.hide()
        self.ui.addBtn.hide()


@Slot()
def open_portfolio_page(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.portfolio_page)
    set_menu_button_colors(self, self.ui.portfolioBtn)
    show_or_hide_stock_buttons(self, show=True)


@Slot()
def open_help_page(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.help_page)
    set_menu_button_colors(self, self.ui.helpBtn)
    show_or_hide_stock_buttons(self, show=False)


@Slot()
def open_settings_page(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.setting_page)
    set_menu_button_colors(self, self.ui.settingsBtn)
    show_or_hide_stock_buttons(self, show=False)


@Slot(object, str, float, int, object)
def add_stock_slot(self, symbol, price, quantity, callback):
    action = AddStockAction(self, callback=callback)
    action.perform(symbol, price, quantity)


@Slot(object, object)
def refresh_stocks_slot(self, callback):
    action = RefreshStockAction(self, callback=callback)
    action.perform()
