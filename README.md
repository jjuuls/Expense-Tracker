# Expense Tracker CLI

A command-line personal finance and budgeting application built with Python and SQLite.

This project started as a simple expense tracker built to help manage finances during a career transition. As new requirements emerged through real-world usage, it evolved into a modular personal finance management system featuring budgeting, reporting, analytics, and SQLite-backed persistence. 

---

## Features

### Expenses

- Add expenses
- View all expenses
- View total expenses
- Filter expenses by category
- Delete expenses by ID
- Automatic date tracking
- View monthly expense totals

### Income

- Add income records
- View all income records
- View total income
- Delete income records by ID
- Automatic date tracking

### Budgets

- Set monthly budgets
- View monthly budgets
- Update existing budgets
- Delete monthly budgets
- View monthly budget summaries
- Compare spending against budget limits

### CSV Import

- Import bank transactions from CSV files
- Separate expenses and income based on transaction amount
- Skip pending transactions
- Clean bank-formatted dollar amounts
- Store imported transactions in SQLite
- Display import summaries with imported and skipped row counts
- Prevent repeat imports of the same CSV file

### Automatic Categorization

- Automatically categorize imported transactions using merchant keyword rules
- Categorize spending into groups such as Food, Gas, Debt Payments, Fitness Travel,           Shopping, Transfers, Subscriptions, and Smoke
- Reduce manual cleanup after importing bank statements
- Keep unmatched transactions as Uncategorized for review

### Reports & Analytics

- View net balance
- View savings rate
- View spending totals by category
- Generate monthly financial reports
- Compare spending between two months
- Analyze real bank transaction data after CSV import

### Dashboard

- Display total income
- Display total expenses
- Display net balance
- Display current month spending
- Display current budget status
- Display budget usage percentage
- Display remaining budget or over-budget amount

### Application

- Persistent SQLite database storage
- Menu-driven command-line interface
- Input validation for amounts and IDs
- Automatic table creation on startup
- Modular application architecture
- Separate modules for expenses, income, budgets, reports, database setup, and CSV importing


---

## Technologies Used

- Python
- SQLite
- SQL
- CSV module
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

## Example Start Up/Main Menu

```text

          
Expense Tracker Dashboard

          
Total Income: $500.00

Total Expenses: $365.50

Net Balance: $134.50

Current Month: 2026-06

Spent This Month: $0.00



Monthly Budget: Not set
--------------------

              
Expense Tracker Main Menu

              
1. Expenses
              
2. Income
              
3. Budgets
              
4. Reports

5. Import Bank Transactions from CSV
              
6. Exit
              

Enter your choice: 

```

---

## Project Structure

```text
Expense-Tracker/
│
├── main.py
├── database.py
├── expenses.py
├── income.py
├── budgets.py
├── reports.py
├── csv_import.py
├── expenses.db
├── README.md
└── .gitignore
```

---

## Database Structure

### Expenses Table

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
amount REAL NOT NULL
category TEXT NOT NULL
description TEXT NOT NULL
date TEXT NOT NULL
```

### Income Table

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
amount REAL NOT NULL
source TEXT NOT NULL
date TEXT NOT NULL
```

### Budgets Table

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
month TEXT NOT NULL UNIQUE
amount REAL NOT NULL
```

### CSV Imports Table

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
file_hash TEXT NOT NULL UNIQUE
file_name TEXT NOT NULL
imported_at TEXT NOT NULL
```

---

## What I Learned

This project helped me practice:

- Building a larger multi-file Python application
- Designing software around real user needs
- Working with SQLite databases
- Creating and managing multiple database tables
- Writing SQL queries with SELECT, INSERT, DELETE, SUM, GROUP BY, ORDER BY, LIKE, and ON CONFLICT
- Building CRUD functionality
- Separating database logic, business logic, reporting logic, and menu logic
- Importing and processing CSV files
- Cleaning bank-formatted transaction data
- Handling real-world data inconsistencies
- Automatically categorizing transactions using rule-based keyword matching
- Skipping pending transactions during imports
- Generating financial summaries from stored data
- Creating monthly reports and spending comparisons
- Calculating net balance and savings rate
- Improving a project through iterative feature upgrades

---

## Future Improvements

- Add import preview before saving transactions
- Store category rules in a JSON file
- Allow users to edit category rules from the menu
- Add expense editing
- Add income editing
- Add custom date entry
- Export reports to CSV
- Add recurring expenses
- Add recurring income
- Add savings goals
- Add budget alerts
- Add automated testing
- Improve report formatting
- Build a web version using Flask or Django

---

## Author

Julian Gonzalez
