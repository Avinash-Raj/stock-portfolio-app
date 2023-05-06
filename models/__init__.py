# Create a connection to the database
import sys

from PySide6.QtSql import QSqlDatabase

from models.model import StockModel

DB = QSqlDatabase.addDatabase("QSQLITE")
DB.setDatabaseName("example.db")
if not DB.open():
    print("Unable to connect to database")
    sys.exit(1)

__all__ = ["DB", "StockModel"]
