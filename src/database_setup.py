import sqlite3

class SetUp:
    def __init__(self):
        self.db = sqlite3.connect('store_app_data')
        self.db_cursor = self.db.cursor()

    def __create_user_id_table__(self):       
        self.db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_info(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(64) NOT NULL UNIQUE,
            password VARCHAR(64) NOT NULL
        )
        """)
        self.db.commit()

    def __create_to_do_table__(self):
        self.db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name VARCHAR(64) NOT NULL UNIQUE,
            task_description VARCHAR(64) NOT NULL,
            task_is_secret INTEGER CHECK (task_is_secret IN (0, 1))
        )
        """)
        self.db.commit()

    def close_connection(self):
        self.db.close()