import datetime as dt
import tkinter as tk
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
with sql.connect("updatedfile.db", detect_types=sql.PARSE_DECLTYPES) as db:
    cursor = db.cursor()
    cursor1 = db.cursor()
shared_data = {"date": None,
               "type": None,
               "level": None,
               "comments": "No Further Comments"}
current_date = dt.date.today().strftime("%Y-%m-%d")
create_date_table = (
    "CREATE TABLE IF NOT EXISTS test_dates(test_date DATE, test_type TEXT, test_level TEXT, comments TEXT, time_stamp DATE)")
cursor.execute(create_date_table)

title_font = ("Times New Roman", 30)




def get_details():
    global result
    global current
    today_date = (
        "SELECT test_date,test_type,test_level,comments FROM test_dates WHERE test_date = ? ")
    check_date = (
        "SELECT test_date,test_type,test_level,comments FROM test_dates WHERE test_date > ? ")
    cursor1.execute(check_date, [(current_date)])
    cursor.execute(today_date, [(current_date)])
    df = pd.read_sql_query(today_date, [(current_date)],db)
    result = cursor.fetchall()
    current = cursor1.fetchall()
