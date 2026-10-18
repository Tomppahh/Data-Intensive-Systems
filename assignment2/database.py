import csv
import sqlite3
from pathlib import Path


def connectToDatabase(database):
    return sqlite3.connect(f"{database}.db")


def makeDatabases(databases):
    for database in databases:
        conn = connectToDatabase(database)
        connectToDatabase(database)
        print(f"Database {database} created successfully!")
        conn.close()


def createTable(database):
    conn = connectToDatabase(database)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def loadDataFromFile(filename, database):
    filePath = Path(__file__).parent / filename
    conn = connectToDatabase(database)

    try:
        with open(filePath, newline="", encoding="utf-8") as file:
            rows = csv.DictReader(file)

            for row in rows:
                conn.execute(
                    "INSERT INTO products (name, quantity) VALUES (?, ?)",
                    (row["name"], int(row["quantity"])),
                )

        conn.commit()
        print(f"Data loaded into {database}.")

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()
