from __future__ import annotations

from typing import TYPE_CHECKING, List

from PySide6.QtCore import QObject, Signal

from stocks.entities.classes import CURRENCIES
from stocks.models.controller import SettingsModelController
from stocks.settings import PORTFOLIO_TABLE_AMOUNT_COLUMN_NAMES
from stocks.slots.receivers import add_settings_slot
from stocks.widgets.messages import show_error_message, show_success_message

if TYPE_CHECKING:
    from PySide6.QtWidgets import QLineEdit

    from stocks.windows.main import MainWindow
    from stocks.windows.ui_interface import Ui_MainWindow


class SettingsPage(QObject):
    add_settings_signal = Signal(object, str, str, object)
    settings_added_signal = Signal(bool)

    def __init__(self, main_window: MainWindow) -> None:
        super().__init__()
        self.main_window = main_window
        self.ui: Ui_MainWindow = main_window.ui

        # connect signals
        self.ui.buttonBox.accepted.connect(self.validate_and_accept_settings)
        self.add_settings_signal.connect(add_settings_slot)
        self.fields = {
            "local_currency": self.ui.localCurrencyLineEdit,
            "columns_to_convert": self.ui.columnsToConvertLineEdit,
            "sumup_columns": self.ui.sumUpColumnsLineEdit,
        }
        self.set_values_from_db()

    def set_values_from_db(self):
        """
        Grab data from db table and then fill values on appropriate text boxes.
        """
        controller = SettingsModelController()
        values = controller.get_settings()
        self.ui.localCurrencyLineEdit.setText(values.get("local_currency", ""))
        self.ui.columnsToConvertLineEdit.setText(values.get("columns_to_convert", ""))
        del controller

    def apply_style_for_error_fields(self, fields: List[QLineEdit]) -> None:
        """
        Apply style for error fields, such as red border.

        Args:
            fields (list): List of error fields.
        """
        for field in fields:
            field.setStyleSheet("border: 1px solid red;")

    def reset_field_styles(self) -> None:
        """
        Reset styles on fields, ie. removing red border. etc
        """
        for field in self.fields.values():
            field.setStyleSheet("")

    def validate_and_accept_settings(self):
        # Perform validation on the form fields
        errors = []
        error_fields = []

        local_currecy_field = self.fields["local_currency"]
        local_currency_text = local_currecy_field.text().strip().upper()

        if local_currency_text:
            if local_currency_text not in CURRENCIES:
                errors.append(f'"{local_currency_text}" is not a valid currency.')
                error_fields.append(local_currecy_field)

        columns_to_convert = self.fields["columns_to_convert"]
        columns_to_convert_text = columns_to_convert.text().strip()

        if columns_to_convert_text:
            columns_list = columns_to_convert_text.split(",")
            for column in columns_list:
                if column not in PORTFOLIO_TABLE_AMOUNT_COLUMN_NAMES:
                    errors.append(
                        f'"{column}" is not a valid amount column. Valid column names are {PORTFOLIO_TABLE_AMOUNT_COLUMN_NAMES}'
                    )
                    error_fields.append(columns_to_convert)

        if errors:
            self.apply_style_for_error_fields(error_fields)
            show_error_message("\n".join(errors), self.main_window)
            return False

        self.add_settings_signal.emit(
            self.main_window, local_currency_text, columns_to_convert_text, self.add_settings_callback
        )

        return False

    def add_settings_callback(self, action_instance, is_success: bool, error: str):
        """
        A spinner callback function which accepts or rejects the add dialog model.
        """
        if is_success:
            show_success_message("Settings Updated successfully!", self.main_window)
            self.settings_added_signal.emit(True)
        else:
            show_error_message(error, self.main_window)
