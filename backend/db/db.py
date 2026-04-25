import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv("../../.env.db")

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


class DB:
    def __init__(self, connection):
        self.connection: mysql.connector.MySQLConnection = connection

    def reset(self):
        with self.connection.cursor() as cursor:
            cursor.execute("DROP TABLE products")

    def setup(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255),
    name VARCHAR(255),
    cents INT UNSIGNED
);
""")

    def add_product(self, url: str, name: str, cents: int):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO products (url, name, cents) VALUES (%s, %s, %s)", (url, name, cents))

    def display_tables(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            for table in cursor.fetchall():
                assert type(table) is tuple
                print(f"{table[0]}:")
                # NOTE this is unsanitized because SQL parameters
                # are unsupported for database/table/column names
                cursor.execute(f"SHOW COLUMNS FROM {table[0]}")
                for column in cursor.fetchall():
                    assert type(column) is tuple
                    print(f"\t{column[0]}")

    def display_rows(self, table):
        with self.connection.cursor() as cursor:
            print(f"{table}:")
            # NOTE unsanitized (see display_tables())
            cursor.execute(f"SELECT * FROM {table}")
            for row in cursor.fetchall():
                print(f"\t{row}")


if __name__ == "__main__":
    with mysql.connector.connect(
        host="localhost",
        port=3306,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
    ) as connection:
        db = DB(connection)
        db.reset()
        db.setup()
        db.add_product("https://pcparts.com/amdgpu", "AMD GPU RTX 64,000 CORES", 6700000)
        db.add_product("https://pcparts.com/nvidacpu", "NVIDIA CPU 10GHz", 6900000)
        db.add_product("https://pcparts.com/ddr6", "DDR6 1024GB", 500)
        db.display_tables()
        db.display_rows("products")
