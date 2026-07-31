import csv

import pytest

from csv_import import (
    categorize_transaction,
    import_transactions_from_csv,
)
from expenses import view_expenses

from income import view_income


def test_categorizes_restaurant_as_food():

    assert categorize_transaction("JOES PIZZA") == "Food"


def test_categorizes_gym_as_fitness():

    assert categorize_transaction("LOCAL GYM MEMBERSHIP") == "Fitness"


def test_unknown_transaction_is_uncategorized():

    assert categorize_transaction("UNKNOWN MERCHANT") == "Uncategorized"


def test_import_transactions_from_csv(
        
    temporary_database,

    tmp_path,

    capsys,
):
    csv_path = tmp_path / "bank_transactions.csv"

    rows = [
        {
            "Transaction Date": "2026-07-10",

            "Transaction Description": "JOES PIZZA",

            "Amount": "-25.50",
        },
        {
            "Transaction Date": "2026-07-11",

            "Transaction Description": "EMPLOYER PAYROLL",

            "Amount": "+1000.00",
        },
        {
            "Transaction Date": "PENDING",

            "Transaction Description": "LOCAL CAFE",

            "Amount": "-10.00",
        },
        {
            "Transaction Date": "2026-07-12",

            "Transaction Description": "INVALID TRANSACTION",

            "Amount": "not-a-number",
        },
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:

        writer = csv.DictWriter(

            csv_file,

            fieldnames=[

                "Transaction Date",

                "Transaction Description",

                "Amount",
            ],
        )

        writer.writeheader()

        writer.writerows(rows)

    import_transactions_from_csv(csv_path)

    expenses = view_expenses()

    income_records = view_income()

    terminal_output = capsys.readouterr().out

    assert len(expenses) == 1

    assert expenses[0][1] == pytest.approx(25.50)

    assert expenses[0][2] == "Food"

    assert expenses[0][3] == "JOES PIZZA"

    assert expenses[0][4] == "2026-07-10"

    assert len(income_records) == 1

    assert income_records[0][1] == pytest.approx(1000.00)

    assert income_records[0][2] == "EMPLOYER PAYROLL"

    assert income_records[0][3] == "2026-07-11"

    assert "Expenses Imported: 1" in terminal_output

    assert "Income Imported: 1" in terminal_output

    assert "Rows Skipped: 2" in terminal_output


def test_same_csv_is_not_imported_twice(

    temporary_database,

    tmp_path,

    capsys,
):
    csv_path = tmp_path / "repeated_bank_transactions.csv"

    rows = [
        {
            "Transaction Date": "2026-07-15",

            "Transaction Description": "JOES PIZZA",

            "Amount": "-25.50",
        },
    ]

    with csv_path.open("w", newline="", encoding="utf-8") as csv_file:

        writer = csv.DictWriter(

            csv_file,

            fieldnames=[

                "Transaction Date",

                "Transaction Description",

                "Amount",
            ],
        )

        writer.writeheader()

        writer.writerows(rows)

    import_transactions_from_csv(csv_path)

    import_transactions_from_csv(csv_path)

    expenses = view_expenses()

    terminal_output = capsys.readouterr().out

    assert len(expenses) == 1

    assert "already been imported" in terminal_output
