import tkinter as tk
from tkinter import ttk
from register_backend import register1, register2
title_font = ("Times New Roman", 50)  # Setting font for titles on the frames
large_font = ("Times New Roman", 24)  # Setting fonts for main headings
medium_font = ("Times New Roman", 16)  # Setting fonts for text that will appear on the screen
small_font = ("Times New Roman", 12)  # Setting fonts for small deails to be displayed


class MathsPro(tk.Tk):

    def __init__(self, *args, **kwargs):  # Creating a class that inherits from tk.Tk

        tk.Tk.__init__(self, *args, **kwargs)  # intialises the object

        tk.Tk.wm_title(self, "Maths Pro")  # Sets the title of each page to be Maths Pro
        container = tk.Frame(self)  # defined a container for all the frame be kept

        # The containter is filled with a bunch of frames
        container.pack(side="top", fill="both", expand=True)
        # After the page being packed this allows it to be displayed correctly
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Empty dictionary where all the frames are kept

        for F in (Register, Register2, Main_Menu):  # contains all the pages being used #this will not work without pages
            # Defines the frame from the for loop which contains all the pages
            frame = F(container, self)

            self.frames[F] = frame  # Sets the top frame to be the current frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.frames[F] = frame  # Sets the frame to be the value of the frame in the dictionary

        # This allows the frame to be displayed and streched
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Register)  # sets the first frame to be shown is a register page

    def show_frame(self, cont):  # method that takes in cont as a controller

        frame = self.frames[cont]  # Defines the frame from the chosen frame in the dictionary
        frame.tkraise()  # Brings the frame to the top for the user to see


class Register(tk.Frame):  # Creating a class that inheirts tk.Frame from tkinter

    def __init__(self, parent, controller):  # intialise the class register with self, args and kwargs
        tk.Frame.__init__(self, parent)  # intialise the frame with self and parent class
        # tk.Frame.config(self) allows the frame to be styled i.e changing background colour
        # Title Page of the Registration Form
        label = tk.Label(self, text="Registration 1", font=title_font)
        label.grid(row=0, column=0)

        separator = ttk.Separator(self, orient="vertical")
        separator.grid(row=1, column=10, rowspan=7, sticky="ns")

        label_text = tk.Label(
            self, text="Registration Page Here please enter your personal details \n and press the button to confirm your details", font=small_font)
        label_text.grid(row=3, column=11)  # Label giving instructions on what to do

        # Label for where the user enters their first name
        label_1 = tk.Label(self, text="First Name", font=small_font)
        label_1.grid(row=1, column=0, pady=20)

        firstname = tk.StringVar()  # Stores the actual firstname the user types in

        entry_1 = tk.Entry(self, textvariable=firstname)  # Where the user enter their first name
        entry_1.grid(row=1, column=1)

        # Label for where the user enters their surname
        label_a = tk.Label(self, text="Surname", font=small_font)
        label_a.grid(row=2, column=0, pady=20)

        surname = tk.StringVar()  # Stores the actual surname the user types in

        entry_2 = tk.Entry(self, textvariable=surname)  # Entry of the surname of user
        entry_2.grid(row=2, column=1)

        # Label for where the user enters their age
        label_b = tk.Label(self, text="Age", font=small_font)
        label_b.grid(row=3, column=0, pady=20)

        age = tk.StringVar()  # Stores the actual age the user types in

        entry_b = tk.Entry(self, textvariable=age)  # Entry for the Age of the student/teacher
        entry_b.grid(row=3, column=1)

        # Label for where the user enters their class
        label_c = tk.Label(self, text="Class", font=small_font)
        label_c.grid(row=4, column=0, pady=20)

        school_class = tk.StringVar()  # Stores the class which the user types in

        # Entry for the class in which the student/teacher is apart of
        entry_c = tk.Entry(self, textvariable=school_class)
        entry_c.grid(row=4, column=1)

        # Where the user enters their gender
        label_2 = tk.Label(self, text="Gender", font=small_font)
        label_2.grid(row=5, column=0, pady=20)
        var = tk.IntVar()  # Stores the choice of the user for the gender option

        tk.Radiobutton(self, text="Male", padx=5, variable=var, value=1).grid(
            row=5, column=1)  # The options for the user gender male
        tk.Radiobutton(self, text="Female", padx=20, variable=var, value=2).grid(
            row=5, column=2)  # the options for the user gender female

        label_3 = tk.Label(self, text="School", width=20, font=small_font)  # School of the user
        label_3.grid(row=6, column=0, pady=20)

        var1 = tk.IntVar()  # Stores the choice of the user for the school option
        tk.Radiobutton(self, text="Student", padx=5, variable=var1, value=1).grid(
            row=6, column=1)  # Option for the user either student
        tk.Radiobutton(self, text="Teacher", padx=20, variable=var1, value=2).grid(
            row=6, column=2)  # Option for the user either teacher
        button1 = tk.Button(self, text="Enter details",
                            command=lambda: self.register(controller, firstname.get(), surname.get(), int(age.get()),
                                                          school_class.get(), var.get(), var1.get()))
        # Runs the register function in the other python file
        button1.grid(row=7, column=9)

        button2 = tk.Button(self, text="Check details")
        button2.grid(row=7, column=0)

        def register(self, controller, firstname, surname, age, school_class, var, var1):  # function used changing frames
            # vaildation of all the personal deatils and these details being added into the record
            if register1(firstname, surname, age, school_class, var, var1) == True:
                controller.show_frame(Register2)  # switches to the next part of the registration


class Register2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Changes the background of the colour to be grey (allows for the specific frame to be styled)
        tk.Frame.config(self, bg="grey")
        # Title Page of the second part of the Registration Form
        label = tk.Label(self, text="Register 2", font=title_font, bg="grey")
        label.grid(row=0, column=0)

        separator = ttk.Separator(self, orient="vertical")
        separator.grid(row=1, column=3, rowspan=7, sticky="ns")

        guide = "Enter a username more than 8 characters long and password that is 8 characters long \n contains uppercase, lowercase characters, numeric and special characters"
        label_text = tk.Label(self, text=guide, font=small_font, bg="grey")
        label_text.grid(row=2, column=4)

        # Label for where the user enters their username
        label_0 = tk.Label(self, text="Username", font=small_font, bg="grey")
        label_0.grid(row=1, column=0, pady=20)

        username_entry = tk.StringVar()
        entry_0 = tk.Entry(self, textvariable=username_entry)
        entry_0.grid(row=1, column=1)

        # Label for where the user enters their username
        label_1 = tk.Label(self, text="Password", bg="grey")
        label_1.grid(row=2, column=0, pady=20)

        password_entry = tk.StringVar()  # Stores the actual password the user password

        # Hides the user password when being typed in
        entry_1 = tk.Entry(self, textvariable=password_entry, show="*")
        entry_1.grid(row=2, column=1)

        # Label for where the user confirms the password they typed
        label_2 = tk.Label(self, text="Confirm Password", bg="grey")
        label_2.grid(row=3, column=0, pady=20)

        password_confirm = tk.StringVar()  # Stores the actual password the user password again (used for comparison)

        # Hides the user password when being typed in
        entry_2 = tk.Entry(self, textvariable=password_confirm, show="*")
        entry_2.grid(row=3, column=1)

        # Label for where the user enters their email address
        label_3 = tk.Label(self, text="Email", bg="grey")
        label_3.grid(row=4, column=0, pady=20)

        email_entry = tk.StringVar()
        entry_3 = tk.Entry(self, textvariable=email_entry)
        entry_3.grid(row=4, column=1)
        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(Register))
        button1.grid(row=5, column=0)

        button2 = ttk.Button(self, text="Create Account", command=lambda: self.register(
            username_entry.get(), password_entry.get(), password_confirm.get(), email_entry.get()))
        button2.grid(row=6, column=2)

        def register(self, controller, username, password, password_confirm, email):
            if register2(username, password, password_confirm, email) == True:
                controller.show_frame(Main_Menu)


class Main_Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="blue")

        text_label = tk.Label(self, text="Maths Pro", font=title_font)
        text_label.pack(padx=20, pady=20)

        label_1 = tk.Label(self, text="Username", font=medium_font)
        label_1.pack()

        username = tk.StringVar()

        entry_1 = tk.Entry(self, textvariable=username)
        entry_1.pack()

        label_2 = tk.Label(self, text="Password", font=medium_font)
        label_2.pack()

        password = tk.StringVar()

        entry_2 = tk.Entry(self, textvariable=password)
        entry_2.pack()


root = MathsPro()  # this runs the Maths Pro class
root.geometry("1280x800")  # changes the size of the window
root.mainloop()  # As MathsPro inherited from tkinter this function can be moved
