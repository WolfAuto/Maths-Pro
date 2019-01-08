import sqlite3
import tkinter as tk
from tkinter import ttk


class MathsPro(tk.Tk):  # Creating a class that inherits from tk.Tk

    def __init__(self, *args, **kwargs):  # intialises the object
        tk.Tk.__init__(self, *args, **kwargs)  # intialises the object as a tkinter frame

        # tk.Tk.iconbitmap(self, default="")
        tk.Tk.wm_title(self, "Maths Pro")  # Sets the title of each page to be Maths Pro
        container = tk.Frame(self)  # defined a container for all the framesto be kept

        # The containter is filled with a bunch of frames
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        # After the page being packed this allows it to be displayed correctly
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Empty dictionary where all the frames are kept

        for F in (Register, Register2):  # contains all the pages being used #this will not work without pages

            # Defines the frame from the for loop which contains all the pages
            frame = F(container, self)

            self.frames[F] = frame  # Sets the top frame to be the current frame

            # This allows the frame to be displayed and streched
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Register)  # sets the first frame to be shown is a register page

    def show_frame(self, cont):  # method that takes in cont as a controller

        frame = self.frames[cont]  # Defines the frame from the chosen frame in the dictionary
        frame.tkraise()  # Brings the frame to the top for the user to see


class Register(tk.Frame):  # Creating a class that inheirts tk.Frame from tkinter

    def __init__(self, parent, controller):  # intialise the class register with self, args and kwargs
        tk.Frame.__init__(self, parent)  # intialise the frame with self and parent class
        tk.Frame.config(self)  # allows the frame to be styled i.e changing background colour
        label = tk.Label(self, text="Registration 1", font=("Times New Roman", 50))
        label.pack(pady=10, padx=10)

        label_1 = tk.Label(self, text="First Name", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)

        label_a = tk.Label(self, text="Surname", width=20, font=("bold", 10))
        label_a.place(x=80, y=180)

        label_b = tk.Label(self, text="Age", width=20, font=("bold", 10))
        label_b.place(x=80, y=300)

        label_c = tk.Label(self, text="Class", width=20, font=("bold", 10))
        label_c.place(x=60, y=360)

        school_class = tk.StringVar()

        entry_c = tk.Entry(self, textvariable=school_class)  # Class
        entry_c.place(x=240, y=360)

        age = tk.StringVar()

        entry_b = tk.Entry(self, textvariable=age)  # Age
        entry_b.place(x=240, y=300)

        surname = tk.StringVar()

        entry_2 = tk.Entry(self, textvariable=surname)  # Surname
        entry_2.place(x=240, y=180)

        firstname = tk.StringVar()

        entry_1 = tk.Entry(self, textvariable=firstname)  # First Name
        entry_1.place(x=240, y=130)

        label_2 = tk.Label(self, text="Gender", width=20, font=("bold", 10))
        label_2.place(x=70, y=230)
        var = tk.IntVar()

        tk.Radiobutton(self, text="Male", padx=5, variable=var, value=1).place(x=205, y=230)
        tk.Radiobutton(self, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)

        label_3 = tk.Label(self, text="School", width=20, font=("bold", 10))
        label_3.place(x=70, y=420)

        var1 = tk.IntVar()
        tk.Radiobutton(self, text="Student", padx=5, variable=var1, value=1).place(x=205, y=420)
        tk.Radiobutton(self, text="Teacher", padx=20, variable=var1, value=2).place(x=290, y=420)
        button1 = tk.Button(self, text="Enter details",
                            command=lambda: controller.show_frame(Register2))
        button1.place(x=470, y=470)



        def datacheck():
            First_name = firstname.get()
            Surname = surname.get()
            Age = int(age.get())
            Class = school_class.get()
            if var.get() == 1:
                gender = "Male"
            elif var.get() == 2:
                gender = "Female"
            if var1.get() == 1:
                School = "Student"
            elif var1.get() == 2:
                School = "Teacher"
            conn =  sqlite3.connect("datacheck.db")
            with conn:
                cursor= conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS personal_details (userID INTEGER PRIMARY KEY NOT NULL, firstname VARCHAR(30) NOT NULL, surname VARCHAR(30) NOT NULL,  age INTEGER NOT NULL, class VARCHAR (3) NOT NULL, gender VARCHAR (30) NOT NULL, school VARCHAR (30) NOT NULL)")
            cursor.execute("INSERT INTO personal_details (firstname, surname, age , class, gender , school) VALUES (?, ?, ?, ?, ?, ?)", (First_name,Surname,Age,Class,gender,School))
            conn.commit()
            conn.close()

            controller.show_frame(Register2)
        buttoncheck = tk.Button(self, text="Check details", command=datacheck)

        buttoncheck.place(x=600, y=600)


class Register2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        label = tk.Label(self, text="Register 2", font=("Times New Roman", 50), bg="grey")
        label.pack(pady=10, padx=10)

        label_0 = tk.Label(self, text="Username", font=("Times New Roman", 20), bg="grey")
        label_0.pack()

        username_entry = tk.StringVar()
        entry_0 = tk.Entry(self, textvariable=username_entry)
        entry_0.pack()

        label_1 = tk.Label(self, text="Password", bg="grey")
        label_1.pack()

        password_entry = tk.StringVar()

        entry_1 = tk.Entry(self, textvariable=password_entry, show="*")
        entry_1.pack()

        label_2 = tk.Label(self, text="Email", bg="grey")
        label_2.pack()

        email_entry = tk.StringVar()
        entry_2 = tk.Entry(self, textvariable=email_entry)
        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(Register))
        button1.pack()

        def data_details():
            username = username_entry.get()
            password = password_entry.get()
            email = email_entry.get()


        button2 = ttk.Button(self, text="Create account", bg="grey")
        button2.pack()

root = MathsPro()  # this runs the Maths Pro class
root.geometry("1280x800")  # changes the size of the window
root.mainloop()  # As MathsPro inherited from tkinter this function can be moved
