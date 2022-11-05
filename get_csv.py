from pathlib import Path
from datetime import datetime
import traceback

from web_to_csv.database.database import Database
from web_to_csv.config import DATABASE_PATH, DEBUG, ROOT_DIR

SEPARATOR = ","

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

        # Format query result.
        entries = []
        for entry in query_results:
            # Make mutable.
            entry = list(entry)
            for index, value in enumerate(entry):
                # Ensure values of all indices are strings.
                entry[index] = str(value)
            # Append linebreak on last index value.
            entry[index] = f"{value}\n"
            # Join index values with comma separator.
            entry = SEPARATOR.join(entry)
            # Create list of rows as strings.
            entries.append(entry)

        # Write to CSV file.
        filename = f"{str(datetime.now())} Poll Results.csv"
        with open(Path(ROOT_DIR) / filename, "w") as f:
            for row in entries:
                for value in row:
                    f.write(value)

        print("[\033[1;32mOK\033[0m] Created CSV file")
        print(f"File location: {Path(ROOT_DIR) / filename}")
