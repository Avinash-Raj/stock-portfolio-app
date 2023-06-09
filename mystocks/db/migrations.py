### Migration script which has to run at the start
### for database creation

import sqlite3

from mystocks.db import DB_NAME


def create_stocks_table(conn):
    # create a new table with columns
    # create a cursor object
    cursor = conn.cursor()
    cursor.execute(
        """
      CREATE TABLE stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    shares INTEGER,
    cost_basis REAL,
    market_value REAL,
    gain REAL
  );
  """
    )
    # commit the changes to the database
    conn.commit()


def alter_stocks_table(conn):
    c = conn.cursor()

    # Add columns to the stocks table
    c.execute("ALTER TABLE stocks ADD COLUMN symbol TEXT")
    c.execute("ALTER TABLE stocks ADD COLUMN price_paid REAL")
    c.execute("ALTER TABLE stocks ADD COLUMN currency TEXT")
    c.execute("ALTER TABLE stocks ADD COLUMN dt_created TEXT")
    c.execute("ALTER TABLE stocks ADD COLUMN dt_updated TEXT")
    conn.commit()


def create_settings_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE settings (
            local_currency TEXT,
            columns_to_convert TEXT,
            sumup_columns TEXT
            );
        """
    )
    conn.commit()


def main():
    # create a connection to the SQLite database
    conn = sqlite3.connect(DB_NAME)
    try:
        create_stocks_table(conn)
        alter_stocks_table(conn)
        create_settings_table(conn)
    except sqlite3.OperationalError as e:
        if "table stocks already exists" in str(e):
            # db table already exists, so migrations already applied
            print("Migrations run successfully!")
    except Exception as ex:
        raise ex
    finally:
        if conn:
            conn.close()


main()
