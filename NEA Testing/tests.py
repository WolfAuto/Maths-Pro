import sqlite3 as sql
import datetime as dt
import tkinter as tk
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
conn = sql.connect("updatedfile.db")
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
medium_font = ("Times New Roman", 20)


def show_details():
    root = tk.Tk()

    title_label = tk.Label(root, text="Tests", font=title_font, bg="grey")
    title_label.pack()

    current_label = tk.Label(root, text="Test For Today", bg="grey", font=title_font)
    current_label.config(anchor="center")
    current_label.pack(pady=10)
    today_label = tk.Label(root, text=current_test(), bg="grey", font=medium_font)
    today_label.pack()

    separator = ttk.Separator(root, orient="horizontal")
    separator.pack(fill="x")

    upcoming_label = tk.Label(root, text="Upcoming Tests", font=title_font, bg="grey")
    upcoming_label.pack()

    test_upcoming = tk.Label(root, text=upcoming_test(), bg="grey", font=medium_font)
    test_upcoming.pack(pady=20)

    exit_button = tk.Button(root, text="Exit", command=lambda: root.destroy())
    exit_button.config(height=3, width=10, bg="blue", fg="white")
    exit_button.place(x=920, y=445)

    refresh_button = tk.Button(root, text="Refresh Tests", command=lambda: [
                               delete_date(), upcoming_test(), current_test()])
    refresh_button.config(height=3, width=10, bg="blue", fg="white")
    refresh_button.place(x=0, y=445)

    root.geometry("1000x500+500-100")
    root.config(bg="grey")
    root.attributes("-topmost", True)
    messagebox.showinfo("Window", "After you have finished with this window you can close it")


def upcoming_test():
    sql = """ SELECT test_date,test_type,test_level,comments FROM test_dates WHERE test_date > ?  """
    resp = pd.read_sql_query(sql, db, params=(current_date,))
    if resp.empty:
        return "No Test Today"
    else:
        return resp


def current_test():
    sql = """ SELECT test_date,test_type,test_level,comments FROM test_dates WHERE test_date = ?  """
    resp = pd.read_sql_query(sql, db, params=(current_date,))
    if resp.empty:
        return "No Test Today"
    else:
        return resp


def update_stamp():
    sql = """ UPDATE test_dates SET time_stamp = ? """
    cursor.execute(sql, [(current_date)])
    db.commit()


def delete_date():
    delete_date = ("DELETE FROM test_dates WHERE time_stamp > test_date")
    cursor.execute(delete_date)
    db.commit()
