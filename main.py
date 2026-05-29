from database import create_tables

from expenses import (

    add_expense,

    view_expenses,

    get_total_expenses,

    filter_expenses,

    delete_expense,

    display_expenses,
)
from income import (

    add_income,

    view_income,

    get_total_income,

    delete_income,

    display_income,
)
from budgets import (

    set_monthly_budget,

    get_monthly_budget,

    delete_budget,

    display_budget,

    display_budget_summary,
)
from reports import (

    calculate_net_balance,

    saving_rate,

    get_category_totals,

    display_category_totals,

    get_monthly_report,

    display_monthly_report,
)


create_tables()


while True:

    print("""

Expense Tracker Menu

--- Expenses ---
1. Add Expense
2. View Expenses
3. View Total Expenses
4. Filter Expenses by Category
5. Delete Expense
6. View Category Totals

--- Income ---
7. Add Income
8. View Income
9. View Total Income
10. Delete Income

--- Budget / Reports ---
11. View Net Balance
12. View Savings Rate
13. Set Monthly Budget
14. View Monthly Budget
15. Monthly Budget Summary
16. Delete Monthly Budget
17. View Monthly Report

--- App ---
18. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:
        
            amount = float(input("Enter the amount: "))
        
        except ValueError:
        
            print("Invalid amount. Please enter a valid number.")
        
            continue
        
        category = input("Enter the category: ")
        
        description = input("Enter the description: ")


        add_expense(amount, category, description)

        print("\nExpense added successfully!\n")


    elif choice == "2":

        expenses = view_expenses()

        print("All Expenses:")

        display_expenses(expenses)


    elif choice == "3":

        total = get_total_expenses()

        print(f"Total Spending: ${total:.2f}")


    elif choice == "4":

        category = input("Enter the category to filter by: ")

        expenses = filter_expenses(category)

        print(f'Expenses in category "{category}":')

        display_expenses(expenses)


    elif choice == "5":

        expenses = view_expenses()

        display_expenses(expenses)

        expense_id = input("Enter expense ID to delete: ")

        if expense_id.isdigit():

            deleted = delete_expense(int(expense_id))

            if deleted:

                print("Expense deleted successfully.")

            else:

                print("No expense found with that ID.")

        else:

            print("Please enter a valid expense ID.")


    elif choice == "6":

        category_totals = get_category_totals()

        display_category_totals(category_totals)


    elif choice == "7":

        try:

            amount = float(input("Enter income amount: "))

        except ValueError:

            print("Invalid amount. Please enter a valid number.")

            continue

        source = input("Enter income source: ")

        add_income(amount, source)

        print("\nIncome added successfully!\n")


    elif choice == "8":

        income_records = view_income()

        print("All Income:")

        display_income(income_records)


    elif choice == "9":

        total_income = get_total_income()

        print(f"Total Income: ${total_income:.2f}")


    elif choice == "10":

        income_records = view_income()

        display_income(income_records)

        income_id = input("Enter income ID to delete: ")

        if income_id.isdigit():

            deleted = delete_income(int(income_id))

            if deleted:

                print("Income record deleted successfully.")

            else:

                print("No income record found with that ID.")

        else:

            print("Please enter a valid income ID.")


    elif choice == "11":

        total_income = get_total_income()

        total_expenses = get_total_expenses()

        net_balance = calculate_net_balance()

        print(f"""

Generating financial summary...

Total Income: ${total_income:.2f}

Total Expenses: ${total_expenses:.2f}

Net Balance: ${net_balance:.2f}

""")


    elif choice == "12":

        
        rate = saving_rate()

        print(f"Saving Rate: {rate:.2f}%")


    elif choice == "13":

        month = input("Enter month for budget (YYYY-MM): ")

        try:

            amount = float(input("Enter budget amount: "))

        except ValueError:

            print("Invalid amount. Please enter a valid number.")

            continue

        set_monthly_budget(month, amount)

        print(f"\nBudget of ${amount:.2f} set for {month}.\n")


    elif choice == "14":

        month = input("Enter month to view budget (YYYY-MM): ")

        budget = get_monthly_budget(month)

        display_budget(month, budget)


    elif choice == "15":

        month = input("Enter month to view budget summary (YYYY-MM): ")

        display_budget_summary(month)


    elif choice == "16":

        month = input("Enter month to delete budget (YYYY-MM): ")

        deleted = delete_budget(month)

        if deleted:

            print(f"Budget for {month} deleted successfully.")

        else:

            print(f"No budget found for {month}.")


    elif choice == "17":

        year_month = input("Enter month to report on (YYYY-MM): ")

        report = get_monthly_report(year_month)

        display_monthly_report(year_month, report)


    elif choice == "18":

        print("Exiting the Expense Tracker. Goodbye!")

        break

    else:

        print("Invalid choice. Please try again.")