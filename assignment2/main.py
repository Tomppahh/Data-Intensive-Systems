import database
import menu


def main():
    fileNameForData = "dummy_data.csv"
    databases = ["database1", "database2", "database3"]

    database.makeDatabases(databases)

    for databaseName in databases:
        database.createTable(databaseName)

        conn = database.connectToDatabase(databaseName)
        count = conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]
        conn.close()

        if count == 0:
            database.loadDataFromFile(fileNameForData, databaseName)

    selectedDatabase = None

    while True:
        choice = menu.userMenu(selectedDatabase)

        if choice == 0:
            print("Thank you for using the program. The program will now close.")
            break

        elif choice == 1:
            selectedDatabase = menu.selectDatabase(databases)
            print(f"Selected database: {selectedDatabase}")

        elif choice == 6:
            database.addDatabase(databases)

        elif choice == 7:
            if database.deleteDatabase(selectedDatabase, databases):
                selectedDatabase = None

        elif selectedDatabase is None:
            print("Please select a database first.")

        elif choice == 2:
            database.viewData(selectedDatabase)

        elif choice == 3:
            database.insertData(selectedDatabase)

        elif choice == 4:
            database.editData(selectedDatabase)

        elif choice == 5:
            database.deleteData(selectedDatabase)


if __name__ == "__main__":
    main()
