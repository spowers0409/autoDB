import sqlite3
import sys
import webbrowser

# SQLite database connection
def connectToDB():
    conn = sqlite3.connect('garage.db')
    return conn

# Function that creates a new table within the database
def createNewTable(conn):
    tableName = input("Enter the new table name: ")
    numColumns = int(input("Enter the number of columns: "))
    
    columns = []
    for i in range(numColumns):
        columnName = input(f"Enter name for column {i + 1}: ")
        columnType = input(f"Enter type for column {i + 1} (e.g., INTEGER, TEXT, etc.): ")
        columns.append(f'"{columnName}" {columnType}')
    
    columnsSQL = ", ".join(columns)
    createSQLTable = f'CREATE TABLE IF NOT EXISTS "{tableName}" (id INTEGER PRIMARY KEY AUTOINCREMENT, {columnsSQL})'
    
    cursor = conn.cursor()
    try:
        cursor.execute(createSQLTable)
        conn.commit()
        print(f'Table "{tableName}" created successfully.')
    except Exception as e:
        print(f"Error creating table: {e}")

# Function that lists all tables within the database
def listTables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if tables:
        print("Tables in the database:")
        for i, table in enumerate(tables):
            print(f"{i + 1}. {table[0]}")
    else:
        print("No tables found in the database.")
    return [table[0] for table in tables]

# Function that deletes a table and all its entries
def deleteTable(conn):
    tables = listTables(conn)
    if not tables:
        return

    try:
        tableChoice = int(input("Enter the number of the table to delete: "))
        if 1 <= tableChoice <= len(tables):
            table_name = tables[tableChoice - 1]
            cursor = conn.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS \"{table_name}\"")
            conn.commit()
            print(f'Table "{table_name}" deleted successfully.')
        else:
            print("Invalid, please try again.")
    except ValueError:
        print("Invalid input. Please enter the ID that corresponds to the table you want to delete.")

# Function that adds a column to an already created table
def updateTable(conn):
    tables = listTables(conn)
    if not tables:
        return
    
    tableName = input("Enter the table name to update: ").strip()
    if tableName in tables:
        columnName = input("Enter the new column name to add: ")
        columnType = input("Enter the column type (e.g., INTEGER, TEXT, etc.): ")

        cursor = conn.cursor()
        try:
            cursor.execute(f"ALTER TABLE {tableName} ADD COLUMN {columnName} {columnType}")
            conn.commit()
            print(f"Column '{columnName}' added to table '{tableName}' successfully.")
        except Exception as e:
            print(f"Error updating table: {e}")
    else:
        print("Table not found.")

# Create a new entry in the selected table
def createEntry(conn, tableName):
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({tableName})")
    columns = cursor.fetchall()

    values = []
    for column in columns:
        if column[1] != 'id':  # Skip the 'id' column if it exists
            columnName = column[1]  # This is the column name (e.g., "First Name")
            columnType = column[2]   # This is the column type (e.g., "TEXT")
            prompt = f"Enter value for {columnName} ({columnType}): "
            value = input(prompt)
            values.append(value)
    
    placeholders = ", ".join(["?"] * len(values))
    cursor.execute(f"INSERT INTO {tableName} ({', '.join([col[1] for col in columns if col[1] != 'id'])}) VALUES ({placeholders})", values)
    conn.commit()
    print(f"New entry added to {tableName}.")

# Function that displays all entries within the selected table
def readEntries(conn, tableName):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tableName}")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print(f"No entries found in {tableName}.")

# Function that updates an entry within the selected table
def updateEntry(conn, tableName):
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({tableName})")
    columns = cursor.fetchall()

    entry_id = input(f"Enter the ID of the entry to update in {tableName}: ")

    update_values = []
    for column in columns:
        if column[1] != 'id':
            new_value = input(f"Enter new value for {column[1]} (leave blank to keep current value): ")
            if new_value:
                update_values.append((column[1], new_value))
    
    for col_name, new_value in update_values:
        cursor.execute(f"UPDATE {tableName} SET {col_name} = ? WHERE id = ?", (new_value, entry_id))
    conn.commit()
    print(f"Entry {entry_id} in {tableName} updated.")

# Function that deletes an entry from within the selected table
def deleteEntry(conn, tableName):
    entry_id = input(f"Enter the ID of the entry to delete from {tableName}: ")

    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {tableName} WHERE id = ?", (entry_id,))
    conn.commit()
    print(f"Entry {entry_id} deleted from {tableName}.")

def openGithub():
    github_url = "https://github.com/spowers0409/autoDB"
    webbrowser.open(github_url)
    print("Opening GitHub repository in your default web browser...")

# Function that displays a menu to manage entries within the selected table
def tableMenu(conn, tableName):
    while True:
        print(f"\nManaging table: {tableName}")
        print("1. Create a new entry")
        print("2. Read all entries")
        print("3. Update an entry")
        print("4. Delete an entry")
        print("5. Exit to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            createEntry(conn, tableName)
        elif choice == '2':
            readEntries(conn, tableName)
        elif choice == '3':
            updateEntry(conn, tableName)
        elif choice == '4':
            deleteEntry(conn, tableName)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Main table selection menu
def mainMenu(conn):
    while True:
        print("\nGarage Database Management")
        print("1. Create a new table")
        print("2. List all tables")
        print("3. Update table structure (add a column)")
        print("4. Delete a table")
        print("5. Select a table to manage entries")
        print("6. View this code on my Github")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            createNewTable(conn)
        elif choice == '2':
            listTables(conn)
        elif choice == '3':
            updateTable(conn)
        elif choice == '4':
            deleteTable(conn)
        elif choice == '5':
            tables = listTables(conn)
            if tables:
                table_choice = input("Enter the number of the table you want to manage: ").strip()
                if table_choice.isdigit() and 1 <= int(table_choice) <= len(tables):
                    table_name = tables[int(table_choice) - 1]
                    tableMenu(conn, table_name)
                else:
                    print("Invalid selection. Please try again.")
        elif choice == '6':
            openGithub()  # Call the function to open the GitHub link
        elif choice == '7':
            conn.close()
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    conn = connectToDB()
    mainMenu(conn)
