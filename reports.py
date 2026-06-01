from database import get_connection

from expenses import get_total_expenses, get_month_expense_total

from income import get_total_income

from budgets import get_monthly_budget

from datetime import datetime


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


def display_dashboard():

    current_month = datetime.now().strftime("%Y-%m")

    total_income = get_total_income()
    
    total_expenses = get_total_expenses()
    
    net_balance = calculate_net_balance()

    monthly_budget = get_monthly_budget(current_month)
    
    monthly_expenses = get_month_expense_total(current_month)

    print(f"""
          
Expense Tracker Dashboard

          
Total Income: ${total_income:.2f}

Total Expenses: ${total_expenses:.2f}

Net Balance: ${net_balance:.2f}

Current Month: {current_month}

Spent This Month: ${monthly_expenses:.2f}

""")

    if monthly_budget is None:

        print("\nMonthly Budget: Not set")
    
    else:
    
        remaining_budget = monthly_budget - monthly_expenses

        budget_used = (monthly_expenses / monthly_budget) * 100 if monthly_budget > 0 else 0

        print(f"Monthly Budget: ${monthly_budget:.2f}")

        print(f"\nBudget Used: {budget_used:.2f}%")

        if remaining_budget < 0:
            
            print(f"\nYou are over budget by ${-remaining_budget:.2f}!")

        else:

            print(f"\nYou are within your budget. Remaining: ${remaining_budget:.2f}")

    print("--------------------")


def compare_months(first_month, second_month):

    conn = get_connection()
    
    cursor = conn.cursor()

    cursor.execute(

        "SELECT SUM(amount) FROM expenses WHERE date LIKE ?",

        (first_month + "%",)
    )
    
    first_total = cursor.fetchone()[0] or 0

    cursor.execute(

        "SELECT SUM(amount) FROM expenses WHERE date LIKE ?",
        
        (second_month + "%",)
    )
    
    second_total = cursor.fetchone()[0] or 0

    conn.close()

    difference = second_total - first_total

    return first_total, second_total, difference


def display_month_comparison(first_month, second_month, comparison):

    first_total, second_total, difference = comparison


    print(f"""
          
Monthly Spending Comparison

          
{first_month}: ${first_total:.2f}

{second_month}: ${second_total:.2f}

""")

    if difference > 0:

        print(f"\nYou spent ${difference:.2f} more in {second_month}.\n")

    elif difference < 0:

        print(f"\nYou spent ${abs(difference):.2f} less in {second_month}.\n")

    else:
        
        print("\nSpending was the same for both months.\n")