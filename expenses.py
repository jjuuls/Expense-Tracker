from datetime import datetime

from database import get_connection


def add_expense(amount, category, description):

    conn = get_connection()

    cursor = conn.cursor()

# Automatically timestamp expenses when they are created
    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(

        "INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",

        (amount, category, description, date)
    )

    conn.commit()

    conn.close()


def view_expenses():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    conn.close()

    return expenses


def get_total_expenses():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    conn.close()

    return total or 0


def filter_expenses(category):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM expenses WHERE LOWER(category) = LOWER(?)",

        (category,)
    )

    expenses = cursor.fetchall()

    conn.close()

    return expenses


def delete_expense(expense_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    deleted = cursor.rowcount

    conn.commit()

    conn.close()

    return deleted


def get_month_expense_total(year_month):

    conn = get_connection()

    cursor = conn.cursor()

# Match all expense records for a specific month (YYYY-MM)
    cursor.execute(

        "SELECT SUM(amount) FROM expenses WHERE date LIKE ?",

        (year_month + "%",)
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total or 0


# Keep formatting separate from database logic
def display_expenses(expenses):

    if not expenses:

        print("No expenses found.")

        return

    for expense in expenses:

        print(f"""

ID: {expense[0]}

Amount: ${expense[1]:.2f}

Category: {expense[2]}

Description: {expense[3]}

Date: {expense[4]}
--------------------
""")