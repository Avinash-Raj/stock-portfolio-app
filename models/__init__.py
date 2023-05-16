# Create a connection to the database
import sys

from PySide6.QtSql import QSqlDatabase

from models.controller import SettingsModelController, StockModelController
from models.model import SettingsModel, StockModel, StockModelWithFooter

DB = QSqlDatabase.addDatabase("QSQLITE")
DB_NAME = "stocks.db"
DB.setDatabaseName(DB_NAME)
if not DB.open():
    print("Unable to connect to database")
    sys.exit(1)

__all__ = [
    "DB",
    "StockModel",
    "StockModelController",
    "StockModelWithFooter",
    "SettingsModel",
    "SettingsModelController",
]
