from database import get_connection

from expenses import get_total_expenses

from income import get_total_income


def calculate_net_balance():

    total_income = get_total_income()

    total_expenses = get_total_expenses()

    return total_income - total_expenses


def saving_rate():

    total_income = get_total_income()

    total_expenses = get_total_expenses()

    if total_income == 0:

        return 0.0

    return (total_income - total_expenses) / total_income * 100


def get_category_totals():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
                   
        SELECT category, SUM(amount)
                   
        FROM expenses
                   
        GROUP BY category
                   
        ORDER BY SUM(amount) DESC
    """)

    category_totals = cursor.fetchall()

    conn.close()

    return category_totals


def display_category_totals(category_totals):

    if not category_totals:

        print("No expenses found.")

        return

    print("\nSpending By Category:\n")

    for category, total in category_totals:

        print(f"\n{category}: ${total:.2f}")


def get_monthly_report(year_month):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(

        "SELECT SUM(amount) FROM income WHERE date LIKE ?",

        (year_month + "%",)
    )
    
    total_income = cursor.fetchone()[0] or 0

    cursor.execute(

        "SELECT SUM(amount) FROM expenses WHERE date LIKE ?",

        (year_month + "%",)
    )
    
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
    
    savings_rate = (net_balance / total_income) * 100 if total_income > 0 else 0

    return total_income, total_expenses, net_balance, savings_rate, category_totals


def display_monthly_report(year_month, report):
    
    total_income, total_expenses, net_balance, savings_rate, category_totals = report

    print(f"""
          
Monthly Report: {year_month}

Total Income: ${total_income:.2f}

Total Expenses: ${total_expenses:.2f}

Net Balance: ${net_balance:.2f}

Savings Rate: {savings_rate:.2f}%

""")

    if category_totals:

        print("\nSpending By Category:\n")

        for category, total in category_totals:
        
            print(f"{category}: ${total:.2f}\n")
    
    else:
    
        print("No expenses found for this month.")