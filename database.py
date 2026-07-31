import sqlite3

DB_NAME = "expenses.db"


# Centralize database connections so changes only happen in one place
def get_connection():

    return sqlite3.connect(DB_NAME)


# Create all required tables when the application starts
def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS expenses (
       
             id INTEGER PRIMARY KEY AUTOINCREMENT,
        
             amount REAL NOT NULL,
         
             category TEXT NOT NULL,
          
             description TEXT NOT NULL,
            
             date TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS income (
                   
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            amount REAL NOT NULL,
                   
            source TEXT NOT NULL,
                   
            date TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
                   
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            month TEXT NOT NULL UNIQUE,
                   
            amount REAL NOT NULL
        )
    """)

    # The unique content hash is the durable guard against importing one file twice.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS csv_imports (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            file_hash TEXT NOT NULL UNIQUE,

            file_name TEXT NOT NULL,

            imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()

    conn.close()
