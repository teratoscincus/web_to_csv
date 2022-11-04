"""
Contains a class to handle SQLite3 database operations.

Run as a script to create the database and tables.
"""

import sqlite3


class Database:
    """Handle SQLite3 database operations."""

    def __init__(self, database):
        """
        Init connection and cursor attributes, and enable foreign key support.

        If the database file doesn't yet exist, one will be created.

        The database parameter takes a string argument, specifying the path to the
        database for the connection.
        """
        # Establish connection and create cursor.
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

        # Enable foreign key on each connection.
        self.connection.execute("PRAGMA foreign_keys = ON;")

    def create_tables(self, schema):
        """
        Creates the database tables according to given SQL schema.

        The schema parameter takes a string argument, specifying the path to an .sql
        file expected to contain a schema for the database.
        """
        # Make sure tables exist.
        with open(schema) as f:
            self.connection.executescript(f.read())


if __name__ == "__main__":
    import traceback

    import web_to_csv.config as config

    # Create database and tables.
    try:
        db = Database(config.DATABASE_PATH)
    except:
        if not config.DEBUG:
            print("[\033[1;31mWARNING\033[0m] Failed to create database")
        else:
            traceback.print_exc()
            print(f" * Given database file path: {config.DATABASE_PATH}")
    else:
        print("[\033[1;32mOK\033[0m] Database successfully created")

        try:
            db.create_tables(config.SCHEMA_PATH)
        except:
            if not config.DEBUG:
                print("[\033[1;31mWARNING\033[0m] Failed to create tables")
            else:
                traceback.print_exc()
                print(f" * Given schema file path: {config.DATABASE_PATH}")
        else:
            print(
                "[\033[1;32mOK\033[0m] Tables successfully created from schema specifications"
            )
