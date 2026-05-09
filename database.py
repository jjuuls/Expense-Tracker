import sqlite3


# Create the database and expenses table if it does not exist
def connect():

    conn = sqlite3.connect('expenses.db')
    
    cursor = conn.cursor()

    cursor.execute('''
                   
        CREATE TABLE IF NOT EXISTS expenses (
                   
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            amount REAL NOT NULL,
                   
            category TEXT NOT NULL,
                   
            description TEXT NOT NULL
        )
    ''')
    conn.commit()

    conn.close()  


# Insert a new expense into the database
def add_expense(amount, category, description):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute('''
                   
        INSERT INTO expenses (amount, category, description)
                   
        VALUES (?, ?, ?)
                   
    ''', (amount, category, description))

    conn.commit()

    conn.close()


# Retrieve all stored expenses
def view_expenses():

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM expenses')

    expenses = cursor.fetchall()

    conn.close()

    return expenses


# Calculate the total amount spent
def get_total():

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute('SELECT SUM(amount) FROM expenses')

    total = cursor.fetchone()[0]

    conn.close()

    return total


# Retrieve expenses filtered by category
def filter_expenses(category):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    # Use LOWER() to perform a case-insensitive search
    cursor.execute('SELECT * FROM expenses WHERE LOWER(category) = LOWER(?)', (category,))

    expenses = cursor.fetchall()

    conn.close()

    return expenses


# Delete an expense by its ID
def delete_expense(expense_id):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))

    deleted = cursor.rowcount  

    conn.commit()

    conn.close()

    return deleted
