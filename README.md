# Garage Database Management System

This is a terminal-based Python application that allows you to manage a SQLite database for storing and manipulating data related to vehicles, or any other data structure you define. The application provides a user-friendly menu system for creating, reading, updating, and deleting database tables and their entries. Additionally, you can view the code directly on GitHub from within the application.

## Features

- **Create New Tables:** Easily create new tables with customizable column names and data types.
- **Manage Entries:** Add, read, update, or delete entries in any table you create.
- **Modify Table Structure:** Add new columns to existing tables.
- **Delete Tables:** Remove entire tables and their data from the database.
- **View Code on GitHub:** Directly access the GitHub repository from within the application.
- **Supports Multiple Data Types:** Columns can be defined with different data types such as `INTEGER`, `TEXT`, etc.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/spowers0409/autoDB.git

2. **Navigate to the project directory:**
   ```bash
   cd your_repository_path

3. **Run the applucation:**
   ```bash
   python your_repository_path.py

# Usage

Once the application is running, you'll be presented with the main menu, offering the following options:
1. **Create a new table:** Define a table with custom column names and data types.
2. **List all tables:** View all the tables currently in the database.
3. **Update table structure:** Add new columns to an existing table.
4. **Delete a table:** Permanently delete a table and its entries
5. **Select a table to manage the entries:** Choose a table to add, read, update, or delete entries.
6. **View this code on my GitHub:** Opens the GitHub repository in your default web browser.
7. **Exit:** Closes the application.

# Example Workflow

1. **Create a New Table:**
   - Select option '1' from the main menu
   - Define the table name, the number of columns, and specify the column names and types.
2. **Manage Entries:**
   - Select option '5' to choose a table, and then use the sub-menu to create, read, update, or delete entries.
  
# Requirements

- **Python 2.x**
- **SQLite** - No installation required as SQLite is included with Python's standard library.
