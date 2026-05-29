from database import get_connection

from expenses import get_month_expense_total


def set_monthly_budget(month, amount):

    conn = get_connection()

    cursor = conn.cursor()

# Update the budget if the month already exists instead of creating duplicates
    cursor.execute("""

        INSERT INTO budgets (month, amount)
                   
        VALUES (?, ?)
                   
        ON CONFLICT(month) DO UPDATE SET amount=excluded.amount
                   
    """, (month, amount))

    conn.commit()

    conn.close()


def get_monthly_budget(month):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT amount FROM budgets WHERE month = ?", (month,))

    result = cursor.fetchone()

    conn.close()

    return result[0] if result else None


def delete_budget(month):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("DELETE FROM budgets WHERE month = ?", (month,))

    deleted = cursor.rowcount

    conn.commit()

    conn.close()

    return deleted


def display_budget(month, budget):

    if budget is not None:

        print(f"Budget for {month}: ${budget:.2f}")

    else:

        print(f"No budget set for {month}.")


def display_budget_summary(month):

    budget = get_monthly_budget(month)

    total_expenses = get_month_expense_total(month)

    print(f"\nBudget Summary for {month}:\n")

    display_budget(month, budget)

    print(f"\nTotal Expenses: ${total_expenses:.2f}\n")

    if budget is None:

        print("No budget set for this month, so no comparison can be made.")

        return

    if total_expenses > budget:

        over_budget = total_expenses - budget

        print(f"You have exceeded your budget by ${over_budget:.2f}!")
    else:

        remaining = budget - total_expenses

        print(f"You are within your budget. Remaining: ${remaining:.2f}")