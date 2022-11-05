"""
Configurations for query_formatter.py.

USE:
    CSV_SEPARATOR holds the character separating the columns of the CSV file.
    The use of a comma sign (",") as separator could cause columns not being divided 
    properly in the case where users might input full sentences with comma punctuations.
    Much more uncommon if free text is a semicolon (";"), and is there for the 
    preferable separator.
    
"""

from pathlib import Path
from datetime import datetime, date

from web_to_csv.config import ROOT_DIR

# Formatting configs.
CSV_SEPARATOR = ";"

# Filename configs.
DATE_TIME = str(datetime.now())
DATE = str(date.today())
FILENAME_SUFFIX = "Poll Results"
FILE_EXTENSION = ".csv"  # NOTE: Don't omit the dot (".").

FILENAME = f"{DATE_TIME}{FILENAME_SUFFIX}{FILE_EXTENSION}"

# File path
FILE_PATH = Path(ROOT_DIR) / FILENAME
