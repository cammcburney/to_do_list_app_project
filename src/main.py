from fastapi import FastAPI, HTTPException
import uvicorn
from models import Task
from sql_utilities import PassInformation
from database_setup import SetUp
import sqlite3

# Temporarily drops tables for easier testing
db = sqlite3.connect("store_app_data")
db_cursor = db.cursor()
db_cursor.execute("DROP TABLE IF EXISTS tasks")
db_cursor.execute("DROP TABLE IF EXISTS user_id")
db.commit()
db.close()

# Creates tables within SQLite database
example = SetUp()
example.__create_user_id_table__()
example.__create_to_do_table__()
example.close_connection()

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome": "This is your interactive task list"}


@app.post("/tasks")
async def add_to_do_item(task: Task):
    try:
        PassInformation.__pass_task_values_to_database__(task)
        return task
    except Exception:
        raise HTTPException(status_code=422, detail="Task format incorrect")


@app.get("/tasks")
async def get_task():
    try:
        tasks = PassInformation.__list_tasks__()
        return tasks
    except Exception:
        raise HTTPException(status_code=404, detail="Tasks not found")


# @app.delete("/tasks/{task_id}")
# async def delete_task(task_id: int):
#     for task in to_do_list:
#         if task.task_id == task_id:
#             to_do_list.pop(task_id)
#             return {"task": f"task {task_id} removed"}

# @app.put("/tasks/{task_id}")
# async def update_task(updated_task: Task):
#     for task in to_do_list:
#         if task.task_id == updated_task.task_id:
#             task = updated_task
#             to_do_list[task.task_id] = task
#             return {"task": f"task {updated_task.task_id} updated"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
