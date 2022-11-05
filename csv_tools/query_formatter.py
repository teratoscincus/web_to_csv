from csv_tools.query_results import get_query_results
from csv_tools.config import CSV_SEPARATOR


def get_formatted_sql_query():
    """
    Formats an sql query for writing to a CSV file.

    Returns a formatted string.
    """
    query_results = get_query_results()

    # Format query result.
    entries = []
    for entry in query_results:
        # Make each row mutable.
        entry = list(entry)

        for index, value in enumerate(entry):
            # Ensure values of all indices are strings.
            entry[index] = str(value)

        # Append linebreak on last index value.
        entry[index] = f"{value}\n"

        # Join index values with separator character.
        entry = CSV_SEPARATOR.join(entry)

        # Create list of rows as strings.
        entries.append(entry)

    # Serialize list to string.
    return "".join(entries)
