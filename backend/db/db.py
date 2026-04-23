import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv("../../.env.db")

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE,
)

if connection.is_connected():
    print("connected to mysql server!")
