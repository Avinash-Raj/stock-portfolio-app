import sqlite3

# create a connection to the SQLite database
conn = sqlite3.connect("my_stocks.db")


def create_table(conn):
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
    # close the connection
    conn.close()


def add_columns(conn):
    c = conn.cursor()

    # Add columns to the stocks table
    c.execute("ALTER TABLE stocks ADD COLUMN symbol TEXT")
    c.execute("ALTER TABLE stocks ADD COLUMN price_paid REAL")
    c.execute("ALTER TABLE stocks ADD COLUMN currency TEXT")
    c.execute("ALTER TABLE stocks ADD COLUMN dt_created TEXT")
    c.execute("ALTER TABLE stocks ADD COLUMN dt_updated TEXT")
    conn.commit()
    conn.close()


add_columns(conn)
