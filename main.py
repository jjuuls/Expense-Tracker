from database import create_tables

# Expense Functions
from expenses import (
    add_expense,

    view_expenses,
    
    get_total_expenses,
    
    filter_expenses,
    
    delete_expense,
    
    display_expenses,
)

# Income Functions
from income import (
    
    add_income,
    
    view_income,
    
    get_total_income,
    
    delete_income,
    
    display_income,
)

# Budget Functions
from budgets import (
    
    set_monthly_budget,
    
    get_monthly_budget,
    
    delete_budget,
    
    display_budget,
    
    display_budget_summary,
)

# Reporting Functions
from reports import (
    
    calculate_net_balance,
    
    saving_rate,
    
    get_category_totals,
    
    display_category_totals,
    
    get_monthly_report,
    
    display_monthly_report,
    
    display_dashboard,

    compare_months,

    display_month_comparison,
)


def expenses_menu():
    
    while True:

        print("""
              
Expenses Menu

              
1. Add Expense
              
2. View Expenses
              
3. View Total Expenses
              
4. Filter Expenses by Category
              
5. Delete Expense
              
6. Back to Main Menu
              

""")

        choice = input("Enter your choice: \n")


        if choice == "1":

            try:
                
                amount = float(input("Enter the amount: \n"))

            except ValueError:
                
                print("\nInvalid amount. Please enter a valid number.\n")
                
                continue

            category = input("Enter the category: \n")

            description = input("Enter the description: \n")

            add_expense(amount, category, description)

            print("\nExpense added successfully!")


        elif choice == "2":

            expenses = view_expenses()
            
            display_expenses(expenses)


        elif choice == "3":

            total = get_total_expenses()

            print(f"\nTotal Spending: ${total:.2f}\n")


        elif choice == "4":
            
            category = input("Enter the category to filter by: \n")
            
            expenses = filter_expenses(category)

            display_expenses(expenses)


        elif choice == "5":
            
            expenses = view_expenses()
            
            display_expenses(expenses)

            expense_id = input("\nEnter expense ID to delete: ")

            if expense_id.isdigit():

                deleted = delete_expense(int(expense_id))

                if deleted:
                
                    print("\nExpense deleted successfully.")
                
                else:
                
                    print("\nNo expense found with that ID.")
            
            else:
            
                print("\nPlease enter a valid expense ID.")


        elif choice == "6":
        
            break

        else:
        
            print("\nInvalid choice. Please try again.")


def income_menu():

    while True:

        print("""
              
Income Menu

              
1. Add Income
              
2. View Income
              
3. View Total Income
              
4. Delete Income
              
5. Back to Main Menu
              
""")

        choice = input("Enter your choice: \n")


        if choice == "1":

            try:
            
                amount = float(input("Enter income amount: \n"))
            
            except ValueError:
            
                print("Invalid amount. Please enter a valid number.")
            
                continue

            source = input("Enter income source: \n")

            add_income(amount, source)
            
            print("Income added successfully!")


        elif choice == "2":
            
            income_records = view_income()
            
            display_income(income_records)


        elif choice == "3":
            
            total_income = get_total_income()
            
            print(f"\nTotal Income: ${total_income:.2f}")


        elif choice == "4":
            
            income_records = view_income()
            
            display_income(income_records)

            income_id = input("Enter income ID to delete: ")

            if income_id.isdigit():
            
                deleted = delete_income(int(income_id))

                if deleted:
            
                    print("\nIncome record deleted successfully.")
            
                else:
            
                    print("\nNo income record found with that ID.")
            
            else:
            
                print("\nPlease enter a valid income ID.")


        elif choice == "5":
            
            break

        else:
        
            print("\nInvalid choice. Please try again.")


def budgets_menu():

    while True:

        print("""
              
Budgets Menu

              
1. Set Monthly Budget
              
2. View Monthly Budget
              
3. Monthly Budget Summary
              
4. Delete Monthly Budget
              
5. Back to Main Menu
              
""")

        choice = input("Enter your choice: \n")


        if choice == "1":

            month = input("\nEnter month for budget (YYYY-MM): ")

            try:

                amount = float(input("\nEnter budget amount: "))
            
            except ValueError:
            
                print("\nInvalid amount. Please enter a valid number.")
            
                continue

            set_monthly_budget(month, amount)

            print(f"\nBudget of ${amount:.2f} set for {month}.\n")


        elif choice == "2":

            month = input("\nEnter month to view budget (YYYY-MM): ")
            
            budget = get_monthly_budget(month)
            
            display_budget(month, budget)


        elif choice == "3":
            
            month = input("\nEnter month to view budget summary (YYYY-MM): ")
            
            display_budget_summary(month)


        elif choice == "4":
            
            month = input("\nEnter month to delete budget (YYYY-MM): ")
            
            deleted = delete_budget(month)

            if deleted:
    
                print(f"\nBudget for {month} deleted successfully.\n")
    
            else:
    
                print(f"\nNo budget found for {month}.\n")


        elif choice == "5":

            break

        else:
            
            print("Invalid choice. Please try again.")


def reports_menu():

    while True:

        print("""
              
Reports Menu

              
1. View Net Balance
              
2. View Savings Rate
              
3. View Category Totals
              
4. View Monthly Report
              
5. Compare Two Months
              
6. Back to Main Menu
              
""")

        choice = input("Enter your choice: \n")


        if choice == "1":

            
            total_income = get_total_income()
            
            total_expenses = get_total_expenses()
            
            net_balance = calculate_net_balance()

            print(f"""
                  
Financial Summary

                  
Total Income: ${total_income:.2f}

Total Expenses: ${total_expenses:.2f}

Net Balance: ${net_balance:.2f}

""")


        elif choice == "2":
 
            rate = saving_rate()
 
            print(f"\nSaving Rate: {rate:.2f}%")


        elif choice == "3":
            
            category_totals = get_category_totals()
            
            display_category_totals(category_totals)


        elif choice == "4":
            
            year_month = input("\nEnter month to report on (YYYY-MM): \n")
            
            report = get_monthly_report(year_month)
            
            display_monthly_report(year_month, report)


        elif choice == "5":
            
            first_month = input("Enter first month (YYYY-MM): ")
            
            second_month = input("Enter second month (YYYY-MM): ")

            comparison = compare_months(first_month, second_month)
            
            display_month_comparison(first_month, second_month, comparison)


        elif choice == "6":
            break


        else:
        
            print("\nInvalid choice. Please try again.\n")


def main():

    create_tables()

    while True:

        display_dashboard()

        print("""
              
Expense Tracker Main Menu

              
1. Expenses
              
2. Income
              
3. Budgets
              
4. Reports
              
5. Exit
              
""")

        choice = input("Enter your choice: \n")


        if choice == "1":

            expenses_menu()


        elif choice == "2":
            
            income_menu()


        elif choice == "3":
            
            budgets_menu()


        elif choice == "4":
            
            reports_menu()


        elif choice == "5":
            
            print("\nExiting the Expense Tracker. Goodbye!\n")
            
            break


        else:
            print("\nInvalid choice. Please try again.\n")


main()