import sqlite3 as sql
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


def show_details():
    format_details()
    root = tk.Tk()

    title_label = tk.Label(root, text="Tests", font=title_font, bg="grey")
    title_label.pack()

    current_label = tk.Label(root, text="Test For Today", bg="grey")
    current_label.config(anchor="center")
    current_label.pack(pady=10)
    header_label = tk.Label(root, text=today_header, bg="grey")
    header_label.pack(pady=20)
    today_label = tk.Label(root, text=today_result, bg="grey")
    today_label.pack()

    separator = ttk.Separator(root, orient="horizontal")
    separator.pack(fill="x")

    upcoming_label = tk.Label(root, text="Upcoming Tests", font=title_font, bg="grey")
    upcoming_label.pack()

    header1_label = tk.Label(root, text=upcoming_header, bg="grey")
    header1_label.pack()
    test_upcoming = tk.Label(root, text=upcoming_result, bg="grey")
    test_upcoming.pack(pady=20)

    exit_button = tk.Button(root, text="Exit", command=lambda: root.destroy())
    exit_button.config(height=3, width=10, bg="blue", fg="white")
    exit_button.place(x=420, y=445)

    refresh_button = tk.Button(root, text="Refresh", command=lambda: [
                               delete_date(), format_details()])
    refresh_button.config(height=3, width=10, bg="blue", fg="white")
    refresh_button.place(x=0, y=445)

    root.geometry("500x500+500-100")
    root.config(bg="grey")
    messagebox.showinfo("Window", "After you have finished with this window you can close it")


def format_details():
    format_upcoming()
    format_current()
    global upcoming_result
    global today_result
    upcoming_result = format_upcoming()
    today_result = format_current()


def format_upcoming():
    get_details()
    global upcoming_header
    header = ("Test Date", "Test Type", "Test Level", "Comments")
    widths = [len(cell) for cell in header]
    for row in result:
        for i, cell in enumerate(row):
            widths[i] = max(len(str(cell)), widths[i])
    formatted_row = '       '.join('{:%d}' % width for width in widths)
    upcoming_header = formatted_row.format(*header)
    for row in result:
        return formatted_row.format(*row)


def format_current():
    global today_header
    get_details()
    header = ("Test Date", "Test Type", "Test Level", "Comments")
    widths = [len(cell) for cell in header]
    for row in current:
        for i, cell in enumerate(row):
            widths[i] = max(len(str(cell)), widths[i])
    formatted_row = '        '.join('{:%d}' % width for width in widths)
    today_header = formatted_row.format(*header)
    for row in current:
        return formatted_row.format(*row)


def get_details():
    global result
    global current
    today_date = (
        "SELECT test_date,test_type,test_level,comments FROM test_dates WHERE test_date = ? ", (current_date))
    check_date = (
        "SELECT test_date,test_type,test_level,comments FROM test_dates WHERE test_date > ? ")
    cursor1.execute(check_date, [(current_date)])
    cursor.execute(today_date, [(current_date)])
    df = pd.read_sql_query(today_date, db)
    result = cursor.fetchall()
    current = cursor1.fetchall()


def delete_date():
    delete_date = ("DELETE FROM test_dates WHERE test_date < time_stamp")
    cursor.execute(delete_date)
    db.commit()


def set_test(date, type, level, comment):
    insert_test = (
        "INSERT INTO test_dates (test_date, test_type, test_level, comments, time_stamp) VALUES (?,?,?,?,?) ")
    try:
        dt.datetime.strptime(date, '%Y-%m-%d')
        shared_data["date"] = date
        if type == 1:
            shared_data["type"] = "Pure"
            if level == 1:
                shared_data["level"] = "AS"
                shared_data["comments"] = comment
                cursor.execute(insert_test, [(shared_data["date"]),
                                             (shared_data["type"]), (shared_data["level"]), (shared_data["comments"]), (current_date)])
                db.commit()
                return True
            elif level == 2:
                shared_data["level"] = "A2"
                shared_data["comments"] = comment
                cursor.execute(insert_test, [(shared_data["date"]),
                                             (shared_data["type"]), (shared_data["level"]), (shared_data["comments"]), (current_date)])
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
                                             (shared_data["type"]), (shared_data["level"]), (shared_data["comments"]), (current_date)])
                db.commit()
                return True
            elif level == 2:
                shared_data["level"] = "A2"
                shared_data["comments"] = comment
                cursor.execute(insert_test, [(shared_data["date"]),
                                             (shared_data["type"]), (shared_data["level"]), (shared_data["comments"]), (current_date)])
                db.commit()
                return True
            else:
                messagebox.showerror("Level", "Test Level cannot be left blank")
        else:
            messagebox.showerror("Type", "Test Type cannot be left blank")
    except ValueError:
        messagebox.showerror("Date", "Date Format should be YYYY-MM-DD")


db.commit()
