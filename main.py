from database import connect, add_expense, view_expenses, get_total, filter_expenses


# Initialize the database and table
connect()


# Main application loop
while True:
    print('\nExpense Tracker Menu:')

    print('1. Add Expense')

    print('2. View Expenses')

    print('3. View Total Expenses')

    print('4. Filter Expenses by Category')

    print('5. Exit')


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

        for expense in expenses:

            print(f"""
                  
        ID: {expense[0]}

        Amount: ${expense[1]:.2f}

        Category: {expense[2]}

        Description: {expense[3]}

        --------------------

        """)

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

        for expense in expenses:

            print(f"""
                  
        ID: {expense[0]}

        Amount: ${expense[1]:.2f}

        Category: {expense[2]}

        Description: {expense[3]}

        --------------------

        """)

    # Exit the application
    elif choice == '5':

        print("Exiting the Expense Tracker. Goodbye!")

        break

    # Handle invalid menu selections
    else:

        print("Invalid choice. Please try again.")
