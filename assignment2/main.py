import sqlite3




def main():
    databases = ["database1", "database2", "database3"]
    makeDatabases(databases)

def makeDatabases(databases):
  for database in databases:
      conn = connectToDatabase(database)
      connectToDatabase(database)
      print(f"Database {database} created successfully!")
      conn.close()

def connectToDatabase(database):
    return sqlite3.connect(f"{database}.db")


def createTable(database):
    conn = connectToDatabase(database)






if __name__ == "__main__":
    main()
