import traceback

from web_to_csv.database.database import Database
from web_to_csv.config import DATABASE_PATH, DEBUG


def get_query_results():
    """
    Returns an unformatted SQL query.

    Returns a list of tuples with column values from a database table.
    NOTE: The table being queried is hardcoded.
    """
    # Try establishing a connection to the database.
    try:
        db = Database(DATABASE_PATH)
    except:
        if not DEBUG:
            print("[\033[1;31mWARNING\033[0m] Failed establish database connection")
        else:
            traceback.print_exc()
            print(f" * Given database file path: {DATABASE_PATH}")
    else:
        print("[\033[1;32mOK\033[0m] Database connection successful")

        # Try querying the database.
        try:
            query_results = db.get_all_entries()
        except:
            if not DEBUG:
                print("[\033[1;31mWARNING\033[0m] Failed to query the database")
            else:
                traceback.print_exc()
                print(f" * Given schema file path: {DATABASE_PATH}")
        else:
            print("[\033[1;32mOK\033[0m] Database query successful")

    return query_results
