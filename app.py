import sys

from PySide6.QtWidgets import QApplication, QStyleFactory

from utils.logging import setup_logging
from windows.main import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create("Fusion"))

    # set logging
    setup_logging()

    window = MainWindow()  # Replace with your QMainWindow instance.

    window.show()

    app.exec()
