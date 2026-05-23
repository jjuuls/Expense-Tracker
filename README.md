# Expense Tracker CLI

A command-line personal finance and budgeting application built with Python and SQLite.

This application allows users to track expenses, income, monthly budgets, savings rate, category spending, and monthly financial reports using a persistent SQLite database.

---

## Features

- Add expenses
- View all expenses
- View total expenses
- Filter expenses by category
- Delete expenses by ID
- View spending totals by category
- Add income records
- View all income records
- View total income
- Delete income records by ID
- View net balance
- View savings rate
- Set monthly budgets
- View monthly budgets
- Delete monthly budgets
- View monthly budget summaries
- Generate monthly financial reports
- Automatic date tracking
- Persistent SQLite database storage
- Menu-driven command-line interface
- Input validation for amounts and IDs

---

## Technologies Used

- Python
- SQLite
- Git & GitHub

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/jjuuls/Expense-Tracker.git
```

2. Navigate into the project folder:

```bash
cd Expense-Tracker
```

3. Run the application:

```bash
python main.py
```

---

## Example Menu

```text
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
```

---

## Project Structure

```text
Expense-Tracker/
│
├── main.py
├── database.py
├── expenses.db
├── README.md
└── .gitignore
```

---

## What I Learned

This project helped me practice:

- Working with SQLite databases
- Creating and managing multiple database tables
- Writing SQL queries with SELECT, INSERT, DELETE, SUM, GROUP BY, ORDER BY, and ON CONFLICT
- Building CRUD functionality
- Organizing Python code into reusable functions
- Separating menu logic from database logic
- Handling user input and validation
- Performing financial calculations
- Generating reports from stored data
- Building a real-world command-line budgeting application

---

## Future Improvements

- Add weekly reports
- Add expense editing
- Add income editing
- Add custom date entry
- Export reports to CSV
- Add recurring expenses
- Add budget alerts
- Improve report formatting

---

## Author

Julian Gonzalez