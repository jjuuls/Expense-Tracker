from expenses import (
    add_expense,
    delete_expense,
    filter_expenses,
    get_total_expenses,
    view_expenses,
)


def test_add_expense(temporary_database):

    add_expense(12.50, "Food", "Lunch")

    expenses = view_expenses()

    assert len(expenses) == 1

    assert expenses[0][1] == 12.50

    assert expenses[0][2] == "Food"

    assert expenses[0][3] == "Lunch"


def test_total_expenses(temporary_database):

    add_expense(10.00, "Food", "Breakfast")

    add_expense(25.00, "Gas", "Fuel")

    assert get_total_expenses() == 35.00


def test_filter_expenses_is_case_insensitive(temporary_database):

    add_expense(15.00, "Food", "Dinner")

    add_expense(30.00, "Gas", "Fuel")

    results = filter_expenses("food")

    assert len(results) == 1

    assert results[0][3] == "Dinner"


def test_delete_expense(temporary_database):

    add_expense(20.00, "Shopping", "Shirt")

    expenses = view_expenses()

    expense_id = expenses[0][0]

    deleted = delete_expense(expense_id)

    assert deleted == 1
    
    assert view_expenses() == []