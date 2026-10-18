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

    while True:
        choice = menu.userMenu()

        if choice == 0:
            print("Thank you for using the program. The program will now close.")
            break


if __name__ == "__main__":
    main()
