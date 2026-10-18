# Tomppa Database Program

This is a small Python program made for Assignment 2 of the Data-Intensive Systems course. It lets you choose between SQLite databases and view, add, edit and delete items. You can also create additional databases and delete a database after confirming the action twice.

Each item has an ID, a name and a quantity. The databases are stored as separate `.db` files.

## Run the Windows executable

The executable is available here:

[Download the Windows version](https://github.com/Tomppahh/Data-Intensive-Systems/releases/tag/sqlite3project)

1. Open the release page and find **Assets**.
2. Download **TomppaDatabase.exe**.
3. Put it in a folder where you can save files, then double-click it.

The program opens its own console window with a numbered menu. You do not need to install Python or type a command to start the executable. This version is for Windows.

## Run from source

You need Python 3 installed. Keep `main.py`, `database.py`, `menu.py` and `dummy_data.csv` in the same folder.

You can clone the repository and start the program with:

```bash
git clone https://github.com/Tomppahh/Data-Intensive-Systems.git
cd Data-Intensive-Systems/assignment2
python3 main.py
```

If you already have the project, open a terminal in its `assignment2` folder and run `python3 main.py`. On Windows, you can use `py main.py` instead.

No extra Python packages are needed. The program uses `sqlite3`, `csv` and `pathlib`, which are included with Python.

## Using the program

Enter the number of the action you want and press **Enter**. The menu shows the currently selected database. At startup this is `None`, so first use option **1** to choose a database.

| Option | Action | How to use it |
| --- | --- | --- |
| 1 | Select database | Choose a database from the numbered list. Other data actions will use this selection. |
| 2 | View data | Lists the items in the selected database, including their IDs, names and quantities. |
| 3 | Add data | Enter an item name and a quantity. The name cannot be empty, and the quantity must be a whole number of zero or more. |
| 4 | Edit data | Choose an item by its ID, then enter a new name or quantity. Press Enter without typing a new value to keep the existing one. |
| 5 | Delete data | Choose an item by its ID. Type `YES` exactly to confirm deletion, or enter anything else to cancel. |
| 6 | Create database | Enter a name without `.db`. Use letters, numbers and underscores. The database is added to the selection list with an empty products table. |
| 7 | Delete database | Deletes the selected database file and everything inside it. The program first asks you to type `DELETE`, then asks for the exact database name. Both must match. Deletion is blocked when only three databases are listed. |
| 0 | Exit | Closes the program. |

The program lists the items before asking for an ID when editing or deleting data. After creating a database, use option **1** to select it. After deleting the selected database, the selection returns to `None`.

## A simple example

1. Select option **1** and choose `database1`.
2. Select option **2** to see its items.
3. Select option **3**, enter `Bananas` as the name and `3` as the quantity.
4. View the data again and note the new item's ID.
5. Select option **4** and enter that ID to change the item.
6. Switch to `database2` and view its data. Changes made to `database1` do not change the other database.

## Startup and saved data

- The program starts with `database1`, `database2` and `database3`. Missing default databases and their products tables are created automatically.
- Dummy data is loaded from `dummy_data.csv` whenever a default database's products table is empty at startup. If you delete every item from a default database, the sample data will return the next time you start the program.
- Added, edited and deleted items are saved to the selected database file. Database files are stored in the current working folder, so use the same folder when returning to your saved data.
- Extra databases are listed for the current session. Their files stay saved after closing, but the current version does not automatically list them again after restarting. Use **Create database** with the same name to add an existing file back to the list; its existing items are kept.
- The whole-database deletion check keeps at least three databases in the current list. It checks the number of databases, rather than protecting particular database names.

## Project files

```text
assignment2/
├── main.py          # Startup and handling menu choices
├── database.py      # Database connections and data operations
├── menu.py          # Menu and database selection prompts
├── dummy_data.csv   # Sample items loaded into the default databases
└── README.md
```

The database files are generated locally when the program is used. The executable is shared through the release page.
