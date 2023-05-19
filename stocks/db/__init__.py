import os
import sys

from PySide6.QtSql import QSqlDatabase

# Get the path of the current script file
current_dir = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(current_dir, "stocks.db")

DB = QSqlDatabase.addDatabase("QSQLITE")
DB.setDatabaseName(DB_NAME)
if not DB.open():
    print("Unable to connect to database")
    sys.exit(1)
