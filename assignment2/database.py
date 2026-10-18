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


def insertData(database):
    nameData = input("Please enter the item name: ").strip()

    if not nameData:
        print("The name cannot be empty.")
        return

    try:
        quantityData = int(input("Please enter the quantity: "))

        if quantityData < 0:
            print("The quantity cannot be negative.")
            return

    except ValueError:
        print("Please enter a whole number.")
        return

    conn = connectToDatabase(database)

    try:
        conn.execute(
            "INSERT INTO products (name, quantity) VALUES (?, ?)",
            (nameData, quantityData),
        )

        conn.commit()
        print(f"Item added to {database}.")

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


def viewData(database):
    conn = connectToDatabase(database)

    try:
        items = conn.execute(
            "SELECT id, name, quantity FROM products ORDER BY id"
        ).fetchall()

        if not items:
            print("The database is empty.")
            return False

        print(f"\nItems in {database}:")
        print(f"{'ID':<6}{'Name':<30}{'Quantity':>10}")
        print("-" * 46)

        for itemId, name, quantity in items:
            print(f"{itemId:<6}{name:<30}{quantity:>10}")

        return True

    finally:
        conn.close()


def deleteData(database):
    if not viewData(database):
        return
    try:
        itemId = int(input("Enter the ID of the item to delete: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    conn = connectToDatabase(database)

    try:
        item = conn.execute(
            "SELECT name, quantity FROM products WHERE id = ?",
            (itemId,),
        ).fetchone()

        if item is None:
            print("No item found with that ID.")
            return

        confirmation = input(
            f"Delete {item[0]} with quantity {item[1]} "
            f"from {database}? Type YES to confirm: "
        )

        if confirmation != "YES":
            print("Deletion cancelled.")
            return

        conn.execute(
            "DELETE FROM products WHERE id = ?",
            (itemId,),
        )

        conn.commit()
        print(f"Item {itemId} deleted from {database}.")

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()
