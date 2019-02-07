import tkinter as tk
import sqlite3

First_Name=tk.StringVar()
Surname
Date_of_Birth
Class
var
var1




#SQLite3

def database():



#Tkinter
root = tk.Tk()
root.geometry('1080x800')
root.title("Maths Pro - Registration Form 1")

label_0 = tk.Label(root, text="Reigstration Form 1", width=20, font=("bold", 10))
label_0.place(x=90, y=53)

label_1 = tk.Label(root, text="First Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

label_a = tk.Label(root, text="Surname", width=20, font=("bold", 10))
label_a.place(x=80, y=180)

label_b = tk.Label(root, text="Age", width=20, font=("bold", 10))
label_b.place(x=80, y=300)

label_c = tk.Label(root, text="Class", width=20, font=("bold", 10))
label_c.place(x=60, y=360)

entry_c = tk.Entry(root)
entry_c.place(x=240, y=360)

entry_b = tk.Entry(root)
entry_b.place(x=240, y=300)

entry_2 = tk.Entry(root)
entry_2.place(x=240, y=180)

entry_1 = tk.Entry(root)
entry_1.place(x=240, y=130)

label_2 = tk.Label(root, text="Gender", width=20, font=("bold", 10))
label_2.place(x=70, y=230)
var = tk.IntVar()
tk.Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=205, y=230)
tk.Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

label_3 = tk.Label(root, text="School", width=20, font=("bold", 10))
label_3.place(x=70, y=420)

var1 = tk.IntVar()
tk.Radiobutton(root, text="Student", padx=5, variable=var1, value=1).place(x=205, y=420)
tk.Radiobutton(root, text="Teacher", padx=20, variable=var1, value=2).place(x=290, y=420)

button1= tk.Button(root, text="Enter details")
button1.place(x=470, y=470)
root.mainloop()
