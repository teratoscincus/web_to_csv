"""Function to insert mock entries into database table."""

import click

from web_to_csv.database.database import Database
from web_to_csv.config import DATABASE_PATH


@click.command()
@click.option("--n", "-n", required=True, type=int)
def create_mock_entries(n):
    """
    Insert mock entries into database table.

    Parameter n takes an integer as an argument, and specifies how many mock entries to
    make.
    """

    db = Database(DATABASE_PATH)

    for i in range(n):
        # Alternate answers.
        if i % 2 == 0:
            q1_answer = "Good"
            q2_answer = "Bad"
            q3_answer = "Better if all was good."
        else:
            q1_answer = "Indifferent"
            q2_answer = "Good"
            q3_answer = "All is fine."

        # Insert and commit.
        db.cursor.execute(
            f"""
            INSERT INTO opinion_poll (q1, q2, q3)
            VALUES ('{q1_answer}', '{q2_answer}', '{q3_answer}');
            """
        )  # TODO: Find better way to get table, and column names.
        db.connection.commit()

    print(f"[\033[1;32mOK\033[0m] {n} Mock entries successfully created")


if __name__ == "__main__":
    create_mock_entries()
