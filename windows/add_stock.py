import logging
from functools import partial
from typing import Tuple

from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QDoubleValidator, QIntValidator
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QDialog

from models.controller import StockModelController
from utils.validators import is_valid_stock_symbol
from views.spinner import WaitingSpinner
from windows.messages import show_error_message
from windows.ui_add_stock_dialog import Ui_Dialog as Ui_AddDialog


class MyThread(QThread):
    finished_signal = Signal(object, bool, str)

    def __init__(self, parent, func, *args, db_name=None, **kwargs):
        super().__init__(parent)
        self.func = func
        self.args = args
        self.db_name = db_name
        self.kwargs = kwargs
        self.db = None

    def run(self):
        if self.db_name:
            db = QSqlDatabase.addDatabase("QSQLITE", "my_thread")
            db.setDatabaseName(self.db_name)
            if not db.open():
                print(db.lastError().text())
            self.db = db
        result = self.func(*self.args, thread=self, **self.kwargs)
        self.finished_signal.emit(self.args[0], *result)


class spinning:
    """
    spinner decorator for instance method which supposed to start spinning at the
    method start and stops at the end.
    """

    def __init__(self, f):
        self.func = f

    def __call__(self, instance, *args, **kwargs):
        ret = None
        try:
            instance.spinner.start()
            thread = MyThread(instance, self.func, instance, *args, db_name="example.db", **kwargs)
            thread.finished.connect(lambda: self.processing_finished(instance))
            thread.finished_signal.connect(self.on_thread_finished)
            thread.start()
        except Exception as e:
            raise e
        return ret

    @Slot(object)
    def processing_finished(self, instance):
        logging.debug("Processing finished!")
        instance.spinner.stop()

    @Slot(object, bool, str)
    def on_thread_finished(self, instance, status: bool, error: str):
        logging.debug("Thread finished")
        instance.validate_callback(status, error)

    def __get__(self, instance, owner):
        return partial(self.__call__, instance)


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
        self.spinner = WaitingSpinner(self, modality=Qt.WindowModality.ApplicationModal)
        self.ui.buttonBox.accepted.connect(self.validate_and_accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.nameLineEdit.setPlaceholderText("Enter Stock Symbol...")
        self.ui.priceLineEdit.setPlaceholderText("Enter Purchase Price...")
        self.ui.sharesLineEdit.setPlaceholderText("Enter Shares count...")
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

    @spinning
    def validate_and_accept(self, thread=None) -> Tuple[bool, str]:
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
            return False, "\n".join(errors)

        symbol = values["name"]
        # check for stock symbol valid
        if not is_valid_stock_symbol(symbol):
            return False, f'Invalid Stock Symbol "{symbol}"'

        # add row
        controller = StockModelController(thread.db if thread else None)
        is_added = controller.add_stock_item(
            symbol=symbol, price=float(values["price"]), quantity=int(values["shares"])
        )

        if is_added:
            logging.info("New stock added successfully.")
            return True, ""

        # Grab the last error
        last_error = thread.db.lastError().text() if (thread and thread.db) else self.parent().model.lastError().text()
        logging.error(f"Failed to add stock, {last_error}")
        return False, last_error

    def validate_callback(self, is_success: bool, error: str):
        if is_success:
            self.accept()
        else:
            show_error_message(error, self)

    def reject(self) -> None:
        # stop the spinner it's still spinning
        if self.spinner.is_spinning:
            self.spinner.stop()
        super().reject()
