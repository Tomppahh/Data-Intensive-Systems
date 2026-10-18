from database import (
    connectToDatabase,
    createTable,
    loadDataFromFile,
    makeDatabases,
)
from menu import userMenu

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


if __name__ == "__main__":
    main()
