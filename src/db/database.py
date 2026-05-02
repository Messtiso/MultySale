import sqlite3
from pathlib import Path


DB_PATH = Path("database/multysell.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            brand TEXT,
            category TEXT,
            size TEXT,
            condition TEXT,
            colour TEXT,
            price REAL,
            photo_path TEXT,
            status TEXT DEFAULT 'not listed',
            listed_platforms TEXT,
            sold_price REAL,
            sold_platform TEXT
            )
            """)
    
    connection.commit()
    connection.close()