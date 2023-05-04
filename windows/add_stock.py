import logging
from PySide6.QtWidgets import QDialog, QErrorMessage
from PySide6.QtGui import QIntValidator, QDoubleValidator
from windows.ui_add_stock_dialog import Ui_Dialog as Ui_AddDialog
from models.controller import StockModelController


class AddStockDialog(QDialog):
    """
    Add Stock Dialog.
    """

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
            #    'Cost Basis': self.ui.costBasisLineEdit,
            #    'Market Value': self.ui.marketValueLineEdit,
            #    'Gain': self.ui.gainLineEdit
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
            # Display a validation error message
            message_box = QErrorMessage(self)
            message_box.setWindowTitle("Validation Error")
            message_box.showMessage("\n".join(errors))

            return False

        # add row
        controller = StockModelController()
        is_added = controller.add_stock_item(
            symbol=values["name"], price=float(values["price"]), quantity=int(values["shares"])
        )

        if is_added:
            logging.info("New stock added successfully.")
            return self.accept()

        logging.error("Failed to update stock.")
        return False

    def reject(self) -> None:
        super().reject()
