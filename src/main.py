import uvicorn
import sqlite3
import json
from fastapi import FastAPI, HTTPException
from models import Task
from sql_utilities import PassInformation
from database_setup import SetUp

# Temporarily drops tables for easier testing
db = sqlite3.connect("store_app_data.db")
db_cursor = db.cursor()
db_cursor.execute("DROP TABLE IF EXISTS tasks")
db_cursor.execute("DROP TABLE IF EXISTS user_info")
db.commit()
db.close()

# Creates tables within SQLite database
example = SetUp()
example.__create_user_id_table__()
example.__create_to_do_table__()
example.__del__()

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome": "This is your interactive task list"}


@app.post("/tasks")
async def add_to_do_item(task: Task):
    try:
        pass_info = PassInformation()
        pass_info.__pass_task_values_to_database__(task)
        return task
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Task format incorrect: {e}")


@app.get("/tasks")
async def get_task():
    try:
        pass_info = PassInformation()
        tasks = pass_info.__list_tasks__()
        with open("data/to_do.json", "w") as file:
            json.dump(tasks, file)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Tasks not found: {e}")


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    try:
        pass_info = PassInformation()
        pass_info.__delete_tasks__(task_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# @app.put("/tasks/{task_id}")
# async def update_task(updated_task: Task):
#     for task in to_do_list:
#         if task.task_id == updated_task.task_id:
#             task = updated_task
#             to_do_list[task.task_id] = task
#             return {"task": f"task {updated_task.task_id} updated"}
