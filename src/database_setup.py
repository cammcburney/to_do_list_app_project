import sqlite3


class SetUp:
    def __init__(self):

        # Opens database connection when instantiated
        self.db = sqlite3.connect("store_app_data")
        self.cursor = self.db.cursor()

    def __del__(self):

        # Closes database connection
        self.db.close()

    def __create_user_id_table__(self):

        # Creates table to store user information
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS user_info (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               username TEXT UNIQUE NOT NULL,
                               password TEXT NOT NULL
                               )"""
        )
        self.db.commit()

    def __create_to_do_table__(self):

        # Creates table to store tasks
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS tasks (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               task_name TEXT NOT NULL,
                               task_description TEXT
                               )"""
        )
        self.db.commit()
