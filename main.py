from database import connect, add_expense, view_expenses, get_total, filter_expenses, delete_expense, display_expenses


# Initialize the database and table
connect()


# Main application loop
while True:
    print('\nExpense Tracker Menu:')

    print('1. Add Expense')

    print('2. View Expenses')

    print('3. View Total Expenses')

    print('4. Filter Expenses by Category')
    
    print('5. Delete Expense')
    
    print('6. Exit')

    


    choice = input("Enter your choice: ")


    # Add a new expense
    if choice == '1':

        try:
            
            amount = float(input("Enter the amount: "))

        except ValueError:

            print("Invalid amount. Please enter a valid number.")

            continue

        category = input("Enter the category: ")

        description = input("Enter the description: ")

        add_expense(amount, category, description)

        print("Expense added successfully!")

    # Display all stored expenses
    elif choice == '2':

        expenses = view_expenses()

        print('All Expenses:')

        display_expenses(expenses)

    # Display the total amount spent
    elif choice == '3':

        total = get_total()

        if total is None:
            total = 0

        print(f"Total Spending: ${total:.2f}")

    # Filter expenses by category
    elif choice == '4':

        category = input("Enter the category to filter by: ")

        expenses = filter_expenses(category)

        print(f'Expenses in category "{category}":')

        display_expenses(expenses)

  
    # Delete an expense by ID
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

    # Exit the application
    elif choice == '6':

        print("Exiting the Expense Tracker. Goodbye!")

        break

    # Handle invalid menu selections
    else:

        print("Invalid choice. Please try again.")
    