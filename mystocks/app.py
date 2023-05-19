import sys

from PySide6.QtWidgets import QApplication, QStyleFactory

from mystocks.utils.logging import setup_logging
from mystocks.windows.main import MainWindow


def main():
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create("Fusion"))

    # set logging
    setup_logging()

    window = MainWindow()  # Replace with your QMainWindow instance.

    window.show()

    app.exec()


if __name__ == "__main__":
    main()
