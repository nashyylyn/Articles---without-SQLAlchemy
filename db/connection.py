import sqlite3
DB_PATH = "db/database.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
