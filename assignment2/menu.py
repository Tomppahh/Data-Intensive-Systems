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
