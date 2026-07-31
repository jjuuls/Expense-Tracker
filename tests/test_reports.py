from datetime import datetime

import pytest

from database import get_connection
from expenses import add_expense
from income import add_income
from reports import (
    calculate_net_balance,
    compare_months,
    get_category_totals,
    get_monthly_report,
    saving_rate,
)


def test_net_balance_and_saving_rate(temporary_database):

    add_income(1000.00, "Paycheck")

    add_expense(250.00, "Food", "Groceries")

    assert calculate_net_balance() == 750.00

    assert saving_rate() == pytest.approx(75.00)


def test_category_totals(temporary_database):

    add_expense(20.00, "Food", "Lunch")

    add_expense(10.00, "Food", "Breakfast")

    add_expense(5.00, "Gas", "Fuel")

    totals = get_category_totals()

    assert totals == [

        ("Food", 30.00),

        ("Gas", 5.00),
    ]


def test_monthly_report(temporary_database):

    current_month = datetime.now().strftime("%Y-%m")

    add_income(2000.00, "Paycheck")

    add_expense(500.00, "Housing", "Rent")

    add_expense(100.00, "Food", "Groceries")

    report = get_monthly_report(current_month)

    total_income = report[0]

    total_expenses = report[1]

    net_balance = report[2]

    savings_rate_result = report[3]

    assert total_income == 2000.00

    assert total_expenses == 600.00

    assert net_balance == 1400.00

    assert savings_rate_result == pytest.approx(70.00)


def test_compare_months(temporary_database):
    # Direct inserts provide stable historical dates; add_expense always uses today's date.
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (amount, category, description, date)

        VALUES (?, ?, ?, ?)
        """,
        (100.00, "Food", "January expense", "2026-01-15"),
    )

    cursor.execute(
        """
        INSERT INTO expenses (amount, category, description, date)

        VALUES (?, ?, ?, ?)
        """,
        (150.00, "Food", "February expense", "2026-02-15"),
    )

    connection.commit()

    connection.close()

    first_total, second_total, difference = compare_months(

        "2026-01",

        "2026-02",
    )

    assert first_total == 100.00

    assert second_total == 150.00
    
    assert difference == 50.00
