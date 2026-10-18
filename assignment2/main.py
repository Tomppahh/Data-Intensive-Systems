import csv
import sqlite3
from pathlib import Path

# TODO: ability to delete database? This might not be needed and if made, it needs to be a "ARE YOU COMPLETELY SURE?" type of check for the user


def main():
    fileNameForData = "dummy_data.csv"  # change this if you have different filename
    databases = [
        "database1",
        "database2",
        "database3",
    ]  # you can add new databases by adding them to this list
    makeDatabases(databases)  # create databases, then populate them after

    for database in databases:
        createTable(database)
        conn = connectToDatabase(database)
        count = conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]

        if count == 0:
            loadDataFromFile(fileNameForData, database)

    while True:
        choice = userMenu()

        if choice == 0:
            print("Thank you for using the program. The program will now close.")
            break


def connectToDatabase(database):
    return sqlite3.connect(f"{database}.db")


def userMenu():
    print(
        "\nWelcome to the Tomppa database program.\n"
        "You can add data as a name and quantity, such as Bananas, 3.\n\n"
        "1. Select database\n"
        "2. View data\n"
        "3. Add data\n"
        "4. Edit data\n"
        "0. Exit\n"
    )

    while True:
        try:
            choice = int(input("Please select a number and press enter: "))

            if choice in (0, 1, 2, 3, 4):
                return choice

            print("Please choose a number between 0 and 5.")

        except ValueError:
            print("Please enter a whole number.")


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


if __name__ == "__main__":
    main()
