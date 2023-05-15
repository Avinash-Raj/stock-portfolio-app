import logging

from PySide6.QtCore import Signal
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtWidgets import QDialog

from slots.receivers import add_stock_slot
from utils.validators import is_valid_stock_symbol
from widgets.messages import show_error_message
from windows.ui_add_stock_dialog import Ui_Dialog as Ui_AddDialog


class AddStockDialog(QDialog):
    """
    Add Stock Dialog.
    """

    add_stock_signal = Signal(object, str, float, int, object)
    stock_added_signal = Signal(bool)

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.ui = Ui_AddDialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Add Stock")
        self.resize(400, 300)
        self.setup()

    def setup(self):
        self.ui.buttonBox.accepted.connect(self.validate_and_accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.nameLineEdit.setPlaceholderText("Enter Stock Symbol...")
        self.ui.priceLineEdit.setPlaceholderText("Enter Purchase Price...")
        self.ui.sharesLineEdit.setPlaceholderText("Enter Shares count...")
        self.add_stock_signal.connect(add_stock_slot)
        self.validators()

    def validators(self):
        # set validator for age edit
        shares_validator = QIntValidator()
        shares_validator.setRange(1, 500)
        self.ui.sharesLineEdit.setValidator(shares_validator)

        # price of each share
        price_validator = QDoubleValidator()
        price_validator.setRange(1.0, 500.0)
        self.ui.priceLineEdit.setValidator(price_validator)

    def validate_and_accept(self):
        # Perform validation on the form fields
        errors = []
        required_fields = {
            "Name": self.ui.nameLineEdit,
            "Price": self.ui.priceLineEdit,
            "Shares": self.ui.sharesLineEdit,
        }
        values = {}

        for name, field in required_fields.items():
            field_text = field.text().strip()
            if not field_text:
                field.setStyleSheet("border: 1px solid red;")
                errors.append(f"{name} is required.")
            else:
                values[name.lower()] = field_text

        if errors:
            show_error_message("\n".join(errors), self)
            return False

        symbol = values["name"]
        # check for stock symbol valid
        if not is_valid_stock_symbol(symbol):
            show_error_message(f'Invalid Stock Symbol "{symbol}"', self)
            return False

        # add row
        price, quantity = float(values["price"]), int(values["shares"])
        self.add_stock_signal.emit(self, symbol, price, quantity, self.add_stock_callback)

        return False

    def add_stock_callback(self, action_instance, is_success: bool, error: str):
        """
        A spinner callback function which accepts or rejects the add dialog model.
        """
        if is_success:
            self.accept()
        else:
            show_error_message(error, self)

    def accept(self) -> None:
        super().accept()
        # Emit the custom signal with the current count as an argument
        logging.info("on accept, trigger stock added signal ")
        self.stock_added_signal.emit(True)
