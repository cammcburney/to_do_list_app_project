import sqlite3
from models import User, Task


class PassInformation:
    def __init__(self):
        self.db = sqlite3.connect("store_app_data")
        self.db_cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def __pass_through_user_values_to_database__(self, user_details: User):
        """
        Passes user information to database if format is correct.

            Parameters: user_details takes data in a dictionary format based on the model User (see models.py).

            Return: N/A

        """

        try:
            self.db_cursor.execute(
                "INSERT INTO user_info (username, password) VALUES (?, ?)",
                (user_details.username, user_details.password),
            )
            self.db.commit()

        except sqlite3.IntegrityError as error:
            print(f"--ERROR-- Could not insert user: {error}")

    def __pass_task_values_to_database__(self, task: Task):
        """
        Passes task information to database if format is correct.

            Parameters: task takes data in a dictionary format based on the model Task (see models.py).

            Return: N/A

        """

        try:
            self.db_cursor.execute(
                "INSERT INTO tasks (task_name, task_description) VALUES (?, ?)",
                (task.task_name, task.task_description),
            )
            self.db.commit()

        except sqlite3.IntegrityError as error:
            print(f"--ERROR-- Could not insert task: {error}")

    def __list_tasks__(self):
        """
        Queries the tasks table to return all task data.

            Parameters: N/A

            Return: List of dictionaries including the task data.

        """

        try:
            self.db_cursor.execute("SELECT * FROM tasks")
            task_list = self.db_cursor.fetchall()
            return [
                {"id": task[0], "task_name": task[1], "task_description": task[2]}
                for task in task_list
            ]

        except Exception as error:
            print(f"--ERROR-- Could not retrieve tasks: {error}")
            return []
