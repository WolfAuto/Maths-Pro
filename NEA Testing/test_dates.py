import sqlite3 as sql
import datetime as dt
import tkinter as tk
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
import sys
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
    messagebox.showinfo("Window", "After you have finished with this window you can close it")
    root = tk.Tk()

    title_label = tk.Label(root, text="Tests", font=title_font, bg="grey")
    title_label.pack()

    current_label = tk.Label(root, text="Test For Today", bg="grey", font=title_font)
    current_label.config(anchor="center")
    current_label.pack(pady=10)
    today_label = tk.Label(root, text=current_test(), bg="grey", font=medium_font, wraplengt=700)
    today_label.pack()

    separator = ttk.Separator(root, orient="horizontal")
    separator.pack(fill="x")

    upcoming_label = tk.Label(root, text="Upcoming Tests", font=title_font, bg="grey")
    upcoming_label.pack()

    test_upcoming = tk.Label(root, text=upcoming_test(), bg="grey", font=medium_font,wraplengt=500)
    test_upcoming.pack(pady=20)

    exit_button = tk.Button(root, text="Exit", command=lambda: root.destroy())
    exit_button.config(height=3, width=10, bg="blue", fg="white")
    exit_button.place(x=1120, y=745)

    refresh_button = tk.Button(root, text="Refresh Tests", command=lambda: update_labels())
    refresh_button.config(height=3, width=10, bg="blue", fg="white")
    refresh_button.place(x=0, y=745)


    def update_labels():
        delete_date()
        today_label["text"] = current_test()
        test_upcoming["text"] = upcoming_test()
    root.geometry("1200x800")
    root.config(bg="grey")
    root.attributes("-topmost", True)


def upcoming_test():
    sql = """ SELECT test_date,test_type,test_level,comments FROM test_dates WHERE test_date > ?  """
    resp = pd.read_sql_query(sql, db, params=(current_date,))
    pd.set_option("display.width", 200)
    pd.set_option("display.max_columns", None)
    if resp.empty:
        return "No Test Today"
    else:
        return resp.to_csv(None)



def current_test():
    sql = """ SELECT test_date,test_type,test_level,comments FROM test_dates WHERE test_date = ?  """
    resp = pd.read_sql_query(sql, db, params=(current_date,))
    pd.set_option("display.width", 200)
    pd.set_option("display.max_columns", None)

    if resp.empty:
        return "No Test Set for the Future"
    else:
        return resp.to_csv(None)

def update_stamp():
    sql = """ UPDATE test_dates SET time_stamp = ? """
    cursor.execute(sql, [(current_date)])
    db.commit()


def delete_date():
    delete_date = ("DELETE FROM test_dates WHERE time_stamp > test_date")
    cursor.execute(delete_date)
    db.commit()


def set_test(date, type, level, comment):
    insert_test ="""INSERT INTO test_dates (test_date, test_type, test_level, comments, time_stamp)
        VALUES (?,?,?,?,?)"""
    try:
        dt.datetime.strptime(date, '%Y-%m-%d')
        
        if date < current_date:
            messagebox.showerror("Date","Date already past set a resonable date")
        else:
            shared_data["date"] = date
            if type == 1:
                shared_data["type"] = "Pure"
                if level == 1:
                    shared_data["level"] = "AS"
                    shared_data["comments"] = comment
                    cursor.execute(insert_test, [(shared_data["date"]),
                                                 (shared_data["type"]),
                                                 (shared_data["level"]),
                                                 (shared_data["comments"]),
                                                 (current_date)])
                    db.commit()
                    return True
                elif level == 2:
                    shared_data["level"] = "A2"
                    shared_data["comments"] = comment
                    cursor.execute(insert_test, [(shared_data["date"]),
                                                 (shared_data["type"]),
                                                 (shared_data["level"]),
                                                 (shared_data["comments"]),
                                                 (current_date)])
                    db.commit()
                    return True
                else:
                    messagebox.showerror("Level", "Test Level cannot be left blank")
            elif type == 2:
                shared_data["type"] = "Applied"
                if level == 1:
                    shared_data["level"] = "AS"
                    shared_data["comments"] = comment
                    cursor.execute(insert_test, [(shared_data["date"]),
                                                 (shared_data["type"]),
                                                 (shared_data["level"]),
                                                 (shared_data["comments"]),
                                                 (current_date)])
                    db.commit()
                    return True
                elif level == 2:
                    shared_data["level"] = "A2"
                    shared_data["comments"] = comment
                    cursor.execute(insert_test, [(shared_data["date"]),
                                                 (shared_data["type"]),
                                                 (shared_data["level"]),
                                                 (shared_data["comments"]),
                                                 (current_date)])
                    db.commit()
                    return True
                else:
                    messagebox.showerror("Level", "Test Level cannot be left blank")
            else:
                messagebox.showerror("Type", "Test Type cannot be left blank")
    except:
        messagebox.showerror("Date", "Date Format should be YYYY-MM-DD and not left blank")
