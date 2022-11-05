from csv_tools.query_formatter import get_formatted_sql_query
from csv_tools.config import FILE_PATH


# # Write to CSV file.
# with open(FILE_PATH, "w") as f:
#     for row in entries:
#         for value in row:
#             f.write(value)

# print("[\033[1;32mOK\033[0m] Created CSV file")
# print(f"File location: {FILE_PATH}")

values = get_formatted_sql_query()

# Write to CSV file.
with open(FILE_PATH, "w") as f:
    f.write(values)

print("[\033[1;32mOK\033[0m] Created CSV file")
print(f"File location: {FILE_PATH}")
