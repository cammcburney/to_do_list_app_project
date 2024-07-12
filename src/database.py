import sqlite3
from database_setup import SetUp
from models import User

# test data 
example = SetUp()
example.__create_user_id_table__()
example.__create_to_do_table__()
example.close_connection()

