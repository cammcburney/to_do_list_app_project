import sqlite3
from models import User

class PassInformation:
    def __pass_through_user_values_to_database__(self, user_details: User):

        try:
            db = sqlite3.connect('store_app_data')
            db_cursor = db.cursor()
            db_cursor.execute("INSERT INTO user_info (username, password) VALUES (?, ?)", (user_details.username, user_details.password))
            db.commit()
            db.close()

        except sqlite3.IntegrityError as error:
            print(f"--ERROR-- Could not insert user: {error}")
            db.close()
