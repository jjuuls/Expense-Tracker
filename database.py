import sqlite3

from datetime import datetime


# Create the database and expenses table if it does not exist
def connect():

    conn = sqlite3.connect('expenses.db')
    
    cursor = conn.cursor()

    cursor.execute('''
                   
            CREATE TABLE IF NOT EXISTS expenses (
                   
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
            amount REAL NOT NULL,
                   
            category TEXT NOT NULL,
                   
            description TEXT NOT NULL,
            
            date TEXT NOT NULL
            )
                   
            ''')
    conn.commit()

    conn.close()  


# Insert a new expense into the database
def add_expense(amount, category, description):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute('INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)', 
                   
                   (amount, category, description, date))

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
def get_total_expenses():

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

# Create income table if it does not exist
def create_income_table():

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("""
                   
        CREATE TABLE IF NOT EXISTS income (
                   
        id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
        amount REAL NOT NULL,
                   
        source TEXT NOT NULL,
                   
        date TEXT NOT NULL
                   
        )
                   
        """)

    conn.commit()

    conn.close()

# Add a new income record
def add_income(amount, source):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(

        "INSERT INTO income (amount, source, date) VALUES (?, ?, ?)",

        (amount, source, date))

    conn.commit()

    conn.close()

# View all income records
def view_income():

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM income")

    income = cursor.fetchall()

    conn.close()

    return income

# Calculate total income
def get_total_income():

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM income")

    total = cursor.fetchone()[0]

    conn.close()

    return total

# Display income records 
def display_income(income_records):

    for income in income_records:

        print(f"""
              
        ID: {income[0]}

        Amount: ${income[1]:.2f}

        Source: {income[2]}

        Date: {income[3]}

        --------------------

        """)

# Delete an income record by ID
def delete_income(income_id):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("DELETE FROM income WHERE id = ?", (income_id,))

    deleted = cursor.rowcount  

    conn.commit()

    conn.close()

    return deleted

# Display expense records 
def display_expenses(expenses):

    for expense in expenses:

        print(f"""
                  
        ID: {expense[0]}

        Amount: ${expense[1]:.2f}

        Category: {expense[2]}

        Description: {expense[3]}

        Date: {expense[4]}

        --------------------

        """)

# Calculate net balance (total income - total expenses)
def calculate_net_balance():

    total_income = get_total_income() or 0

    total_expenses = get_total_expenses() or 0

    net_balance = total_income - total_expenses

    return net_balance

# Calculate total expenses by category
def get_category_totals():

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute('''
        SELECT category, SUM(amount)
                   
        FROM expenses
                   
        GROUP BY category
                   
        ORDER BY SUM(amount) DESC
                   
        ''')

    category_totals = cursor.fetchall()

    conn.close()

    return category_totals

# Display total expenses by category
def display_category_totals(category_totals):

    if not category_totals:

        print("No expenses found.")

        return

    print("\nSpending By Category:")

    for category, total in category_totals:

        print(f"{category}: ${total:.2f}")

# Calculate saving rate (net balance as a percentage of total income)
def saving_rate():

    total_income = get_total_income() or 0

    total_expenses = get_total_expenses() or 0

    if total_income == 0:

        return 0.0

    rate = (total_income - total_expenses) / total_income * 100

    return rate

# Generate a monthly report with total income, total expenses, net balance, savings rate, and category breakdown
def get_monthly_report(year_month):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("""
                   
        SELECT SUM(amount)
                   
        FROM income
                   
        WHERE date LIKE ?
                   
        """, (year_month + "%",))

    total_income = cursor.fetchone()[0] or 0

    cursor.execute("""
                   
        SELECT SUM(amount)
                   
        FROM expenses
                   
        WHERE date LIKE ?
                   
        """, (year_month + "%",))

    total_expenses = cursor.fetchone()[0] or 0

    cursor.execute("""
                   
        SELECT category, SUM(amount)
                   
        FROM expenses
                   
        WHERE date LIKE ?
                   
        GROUP BY category
                   
        ORDER BY SUM(amount) DESC
                   
        """, (year_month + "%",))

    category_totals = cursor.fetchall()

    conn.close()

    net_balance = total_income - total_expenses

    if total_income > 0:

        savings_rate = (net_balance / total_income) * 100
    
    else:

        savings_rate = 0

    return total_income, total_expenses, net_balance, savings_rate, category_totals

# Display the monthly report 
def display_monthly_report(year_month, report):

    total_income, total_expenses, net_balance, savings_rate, category_totals = report

    print(f"""

          Monthly Report: {year_month}


          Total Income: ${total_income:.2f}


          Total Expenses: ${total_expenses:.2f}


          Net Balance: ${net_balance:.2f}


          Savings Rate: {savings_rate:.2f}%


          Spending By Category:

          """)

    if category_totals:

        for category, total in category_totals:

            print(f"{category}: ${total:.2f}")

    else:

        print("No expenses found for this month.")

# Create budget table if it does not exist
def create_budget_table():

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("""
                   
        CREATE TABLE IF NOT EXISTS budgets (
        
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        
        month TEXT NOT NULL UNIQUE,
            
        amount REAL NOT NULL
        
        )
                   
        """)

    conn.commit()

    conn.close()

# Set or update monthly budget
def set_monthly_budget(month, amount):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("""
                   
        INSERT INTO budgets (month, amount) VALUES (?, ?)
        
        ON CONFLICT(month) DO UPDATE SET amount=excluded.amount
        
        """, (month, amount))

    conn.commit()

    conn.close()

# Retrieve monthly budget
def get_monthly_budget(month):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("SELECT amount FROM budgets WHERE month = ?", (month,))

    result = cursor.fetchone()

    conn.close()

    return result[0] if result else None

# Delete monthly budget
def delete_budget(month):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("DELETE FROM budgets WHERE month = ?", (month,))

    deleted = cursor.rowcount  

    conn.commit()

    conn.close()

    return deleted

# Display budget for a specific month
def display_budget(month, budget):

    if budget is not None:

        print(f"Budget for {month}: ${budget:.2f}")

    else:

        print(f"No budget set for {month}.")

# Display budget summary for a specific month, including total expenses and whether the user is within budget
def display_budget_summary(month, budget, total_expenses):

    print(f"Budget Summary for {month}:")

    display_budget(month, budget)

    print(f"Total Expenses: ${total_expenses:.2f}")

    if budget is None:

        print("No budget set for this month, so no comparison can be made.")

        return

    if total_expenses > budget:

        over_budget = total_expenses - budget

        print(f"You have exceeded your budget by ${over_budget:.2f}!")

    else:

        remaining = budget - total_expenses

        print(f"You are within your budget. Remaining: ${remaining:.2f}")

def get_month_expense_total(year_month):

    conn = sqlite3.connect('expenses.db')

    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE date LIKE ?
    """, (year_month + "%",))

    total = cursor.fetchone()[0]

    conn.close()

    return total or 0
