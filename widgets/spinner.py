import logging
from typing import Callable, Optional

from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QColor
from PySide6.QtSql import QSqlDatabase

from widgets.waiting_spinner import WaitingSpinner


# pylint: disable=too-few-public-methods
class SpinningThread(QThread):
    """
    Thread which helps to run the spinner. This should a seperate thread.
    """

    # signal which gets emitted upon target function completion.
    # corresponding slot should receive
    # instance (instance of the class which has spinning method on any one of it's methods)
    # status (bool, target function's return status)
    # error (error text if there's any error else it should be empty)
    finished_signal = Signal(object, bool, str)

    def __init__(self, parent, func, *args, db_name=None, **kwargs):
        super().__init__(parent)
        self.func = func
        self.args = args
        self.db_name = db_name
        self.kwargs = kwargs
        self.db = None
        self.db_connection_name = "spinning_thread"

    def open_database(self):
        """
        Helps to add and open database connection.
        """
        if self.db_name:
            # if the traget function contain any code related to db connection
            # then we must create a new connection aprat from the connection
            # made from the parent thread
            db = QSqlDatabase.addDatabase("QSQLITE", self.db_connection_name)
            db.setDatabaseName(self.db_name)
            if not db.open():
                logging.debug(db.lastError().text())
            self.db = db

    def close_database(self):
        """
        Helps to close and remove database connection.
        """
        if self.db and self.db.open():
            self.db.commit()
            self.db.close()
            QSqlDatabase.removeDatabase(self.db_connection_name)

    def run(self):
        self.open_database()
        result = self.func(*self.args, thread=self, **self.kwargs)
        self.close_database()
        # emit finished_signal with parent_class instance as first argument
        self.finished_signal.emit(self.args[0], *result)


class spinning:
    """
    spinner decorator for instance method which supposed to start spinning at the
    method start and stops at the end.

    Underlying method should be executed inside a seperate thread. If the method has code
    to make db connections then  relevant db_name (ex: test.db) should be passed.
    This ensures a seperate db connection made from the new thread.
    """

    def __init__(self, callback: Optional[Callable] = None, db_name: Optional[str] = None):
        self.callback = callback
        self.db_name = db_name

    def __call__(self, func):
        def wrapper(instance, *args, **kwargs):
            assert instance.spinner, "spinner member unavailable"
            ret = None
            try:
                # spinner parent should be same as thread parent
                thread = SpinningThread(
                    instance.spinner.parent(), func, instance, *args, db_name=self.db_name, **kwargs
                )
                thread.started.connect(lambda: self.on_thread_started(instance))
                thread.finished.connect(lambda: self.on_thread_finished(instance))
                thread.finished_signal.connect(self.processing_finished)
                thread.start()
            except Exception as e:
                raise e
            return ret

        return wrapper

    @Slot(object)
    def on_thread_started(self, instance):
        logging.debug("Spinning Thread started!")
        instance.spinner.start()

    @Slot(object)
    def on_thread_finished(self, instance):
        logging.debug("Spinning Thread finished!")
        instance.spinner.stop()

    @Slot(object, bool, str)
    def processing_finished(self, instance, status: bool, error: str):
        logging.debug("Thread processing finished!")
        callback = self.callback or instance.callback
        if callback:
            logging.debug("Calling callback function...")
            callback(instance, status, error)


class Spinner(WaitingSpinner):
    """
    Spinner class defined with default arguments inorder to use accross all windows.
    """

    def __init__(self, parent):
        super().__init__(
            parent,
            disable_parent_when_spinning=True,
            modality=Qt.WindowModality.WindowModal,
            lines=10,
            line_length=20,
            line_width=8,
            radius=20,
            color=QColor(Qt.GlobalColor.cyan),
        )
