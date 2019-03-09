import sqlite3 as sql
import tkinter as tk
from tkinter import ttk
with sql.connect("updatedfile.db") as db:
    cursor = db.cursor()

def get_students():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students """
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def sort_age():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY Age ASC """
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
    


def sort_surname():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY Surname"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def sort_class():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY class """
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def sort_forename():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY Forename"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def sort_gender():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY Gender"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

root  = tk.Tk()
mainframe = tk.Frame(root)
mainframe.grid(column=0,row=0, sticky=("N,W,E,S") )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
 
# Create a Tkinter variable
tkvar = tk.StringVar(root)
tkvar.set("Please select a student")
choices = sort_surname()


def callback(event):
    print(students.get())
students = ttk.Combobox(mainframe, values=get_students(), state="readonly")
students.set("Please choose a name")
students.config(height=5, width=50)
students.grid()

tk.Button(mainframe,text="Change Age", command = lambda: change_age()).grid()
tk.Button(mainframe,text="Change Class", command = lambda: change_class()).grid()
tk.Button(mainframe,text="Change Gender", command = lambda: change_gender()).grid()
students.bind("<<ComboboxSelected>>", callback)


def change_age():
    students.config(values=sort_age())

def change_class():
    students.config(values=sort_class())

def change_gender():
    students.config(values=sort_gender())
    
 
root.mainloop()
