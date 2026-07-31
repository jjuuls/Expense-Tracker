import csv
import hashlib

from contextlib import closing
from pathlib import Path

from database import get_connection


# Rule-based categorization keeps imports fast, predictable, and easy to update
# without needing an external API or manual category selection for every row.
def categorize_transaction(description):

    description = description.upper()

    category_rules = {

        "Debt Payments": [

            "AMEX EPAYMENT",

            "CHASE CREDIT",

            "CAPITAL ONE CRCARDPMT",

            "APPLECARD GSBANK",

            "MERCURY FBT",

            "AFFIRM.COM",
        ],

        "Food": [

            "MCDONALD",

            "TACO BELL",

            "SUSHI",

            "DELI",

            "WENDY",

            "CHILI",

            "RESTAURA",

            "KPOT",
            
            "GYRO",

            "HOUSE OF QUE",

            "UBER *EATS",

            "JESSIES KETTLE",

            "RESTAURANT",
            
            "CAFE",

            "PIZZA",
        ],

        "Gas": [

            "BP",

            "SHELL",

            "EXXON",

            "SUNOCO",

            "MOBIL",

            "CHEVRON",

            "GAS",
        ],

        "Fitness": [

            "FITNES",

            "FITN",

            "GYM",
        ],

        "Subscriptions": [

            "APPLE.COM/BILL",
        ],

        "Travel": [

            "AIRBNB",

            "KLARNA",
        ],

        "Shopping": [

            "TARGET",

            "WALGREENS",

            "CVS",

            "NURECOVER",
        ],

        "Transfers": [
            
            "ZEL"
        ],

        "Smoke": [

            "APOTHECARIUM",

            "SMOKE SHOP",
        ],
    }

    for category, keywords in category_rules.items():

        for keyword in keywords:

            if keyword in description:

                return category
            
    return "Uncategorized"


def calculate_file_hash(file_path):

    file_hash = hashlib.sha256()

    with open(file_path, "rb") as file:

        # Chunked reads keep hashing memory-efficient even for unusually large exports.
        for chunk in iter(lambda: file.read(8192), b""):

            file_hash.update(chunk)

    return file_hash.hexdigest()



# Bank exports often include payment method text, locations, and masked card numbers.
# Matching against merchant keywords lets the app classify real-world transaction descriptions.
def import_transactions_from_csv(file_path):

    expenses_imported = 0

    income_imported = 0

    skipped = 0

    try:

        file_hash = calculate_file_hash(file_path)

        with closing(get_connection()) as conn:

            cursor = conn.cursor()

            # Content-based matching still catches a duplicate after the file is renamed.
            cursor.execute(

                "SELECT 1 FROM csv_imports WHERE file_hash = ?",

                (file_hash,)
            )

            if cursor.fetchone():

                print("\nThis CSV file has already been imported. No transactions were added.\n")

                return

            with open(file_path, "r", encoding="utf-8-sig") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    try:

                        date = row["Transaction Date"].strip()

                        if "PENDING" in date.upper():

                            skipped += 1

                            continue

                        description = row["Transaction Description"].strip()

                        amount_text = (

                            row["Amount"]

                            .replace("$", "")

                            .replace(",", "")

                            .replace("+", "")

                            .replace(" ", "")

                            .strip()
                        )

                        amount = float(amount_text)

                        if amount < 0:

                            cursor.execute(

                                """
                                INSERT INTO expenses

                                (amount, category, description, date)

                                VALUES (?, ?, ?, ?)
                                """,
                                (
                                    abs(amount),

                                    categorize_transaction(description),

                                    description,

                                    date
                                )
                            )

                            expenses_imported += 1

                        else:

                            cursor.execute(

                                """
                                INSERT INTO income

                                (amount, source, date)

                                VALUES (?, ?, ?)
                                """,
                                (
                                    amount,

                                    description,

                                    date
                                )
                            )

                            income_imported += 1

                    except (ValueError, KeyError):

                        skipped += 1

            # Save the fingerprint only after every row is processed, allowing a failed
            # import to be corrected and retried instead of being permanently blocked.
            cursor.execute(

                """
                INSERT INTO csv_imports (file_hash, file_name)

                VALUES (?, ?)
                """,
                (file_hash, Path(file_path).name)
            )

            conn.commit()

        print(f"""

Import Complete

Expenses Imported: {expenses_imported}

Income Imported: {income_imported}

Rows Skipped: {skipped}

""")

    except FileNotFoundError:

        print("\nCSV file not found.")
