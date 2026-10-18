def userMenu(selectedDatabase):
    print(
        "\nWelcome to the Tomppa database program.\n"
        "You can add data as a name and quantity, such as Bananas, 3.\n\n"
        f"\nCurrently selected database: {selectedDatabase or 'None'}\n\n"
        "1. Select database\n"
        "2. View data\n"
        "3. Add data\n"
        "4. Edit data\n"
        "5. Delete data\n"
        "6. Create database\n"
        "7. Delete database\n"
        "0. Exit\n"
    )

    while True:
        try:
            choice = int(input("\n\nPlease select a number and press enter: "))

            if choice in (0, 1, 2, 3, 4, 5, 6, 7):
                return choice

            print("Please choose a number between 0 and 7.")

        except ValueError:
            print("Please enter a whole number.")


def selectDatabase(databases):
    print("\nAvailable databases:")

    for number, databaseName in enumerate(databases, start=1):
        print(f"{number}. {databaseName}")

    while True:
        try:
            choice = int(input("Select a database: "))

            if 1 <= choice <= len(databases):
                return databases[choice - 1]

            print("Please select one of the listed numbers.")

        except ValueError:
            print("Please enter a whole number.")
