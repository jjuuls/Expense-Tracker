from budgets import (
    delete_budget,
    get_monthly_budget,
    set_monthly_budget,
)


def test_set_monthly_budget(temporary_database):

    set_monthly_budget("2026-07", 1000.00)

    assert get_monthly_budget("2026-07") == 1000.00


def test_update_existing_budget(temporary_database):

    set_monthly_budget("2026-07", 1000.00)

    set_monthly_budget("2026-07", 1500.00)

    assert get_monthly_budget("2026-07") == 1500.00


def test_delete_budget(temporary_database):

    set_monthly_budget("2026-07", 1000.00)

    deleted = delete_budget("2026-07")

    assert deleted == 1
    
    assert get_monthly_budget("2026-07") is None