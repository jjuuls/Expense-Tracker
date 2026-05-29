from datetime import datetime

from database import get_connection


def add_income(amount, source):

    conn = get_connection()

    cursor = conn.cursor()

# Automatically timestamp income entries when they are created
    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(

        "INSERT INTO income (amount, source, date) VALUES (?, ?, ?)",

        (amount, source, date)
    )

    conn.commit()

    conn.close()


def view_income():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM income")

    income_records = cursor.fetchall()

    conn.close()

    return income_records


def get_total_income():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM income")

    total = cursor.fetchone()[0]

    conn.close()

    return total or 0


def delete_income(income_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("DELETE FROM income WHERE id = ?", (income_id,))

    deleted = cursor.rowcount

    conn.commit()

    conn.close()

    return deleted


def display_income(income_records):

    if not income_records:

        print("No income records found.")

        return

    for income in income_records:

        print(f"""
              
ID: {income[0]}

Amount: ${income[1]:.2f}

Source: {income[2]}

Date: {income[3]}
--------------------
""")