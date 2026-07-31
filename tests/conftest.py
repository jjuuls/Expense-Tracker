from pathlib import Path

import pytest

import database


@pytest.fixture

def temporary_database(tmp_path, monkeypatch):

    real_database = Path(database.DB_NAME).resolve()
    
    test_database = tmp_path / "test_expenses.db"

    # Redirect all database calls before setup so a failed test cannot touch real data.
    monkeypatch.setattr(database, "DB_NAME", str(test_database))

    assert Path(database.DB_NAME).resolve() != real_database

    database.create_tables()
