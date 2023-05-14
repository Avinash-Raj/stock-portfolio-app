import sys

from PySide6.QtWidgets import QApplication, QStyleFactory

from themes import darkPalette
from utils.logging import setup_logging
from windows.main import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    # app.setPalette(darkPalette)

    # set logging
    setup_logging()

    window = MainWindow()  # Replace with your QMainWindow instance.
    # Load the QSS file
    # style_file = QFile("styles/main.qss")
    # style_file.open(QIODeviceBase.OpenModeFlag.ReadOnly | QIODeviceBase.OpenModeFlag.Text)
    # style_sheet = style_file.readAll().data().decode("utf-8")
    # style_file.close()

    # # Set the QSS stylesheet for the window
    # window.setStyleSheet(style_sheet)
    window.show()

    app.exec()
