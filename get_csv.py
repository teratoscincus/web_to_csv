from csv_tools.query_formatter import get_formatted_sql_query
from csv_tools.config import FILE_PATH


def get_csv():
    num_rows, values = get_formatted_sql_query()

    # Write to CSV file.
    with open(FILE_PATH, "w") as f:
        f.write(values)

    print("[\033[1;32mOK\033[0m] Created CSV file")
    print(f"Number of rows: {num_rows}")
    print(f"File location: {FILE_PATH}")


if __name__ == "__main__":
    import cProfile

    # cProfile.run("get_csv()")
    get_csv()
