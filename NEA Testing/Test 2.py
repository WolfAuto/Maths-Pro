import tkinter as tk
from tkinter import ttk
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

        for F in (Register, Register2):  # contains all the pages being used #this will not work without pages
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
        tk.Frame.config(self)  # allows the frame to be styled i.e changing background colour

        label_text = tk.Label(
            self, text="Register Here enter personal deatils and press button to confirm")
        label_text.place(x=150, y=350)
        label = tk.Label(self, text="Registration 1", font=(
            "Times New Roman", 50))  # Title Page of the Registration Form
        label.place(x=450, y=10)

        # Label for where the user enters their first name
        label_1 = tk.Label(self, text="First Name", width=20, font=small_font)
        label_1.place(x=619, y=230)

        firstname = tk.StringVar()  # Stores the actual firstname the user types in

        entry_1 = tk.Entry(self, textvariable=firstname)  # Where the user enter their first name
        entry_1.place(x=770, y=230)

        # Label for where the user enters their surname
        label_a = tk.Label(self, text="Surname", width=20, font=small_font)
        label_a.place(x=610, y=280)

        surname = tk.StringVar()  # Stores the actual surname the user types in

        entry_2 = tk.Entry(self, textvariable=surname)  # Entry of the surname of user
        entry_2.place(x=770, y=280)

        # Label for where the user enters their age
        label_b = tk.Label(self, text="Age", width=20, font=small_font)
        label_b.place(x=595, y=330)

        age = tk.StringVar()  # Stores the actual age the user types in

        entry_b = tk.Entry(self, textvariable=age)  # Entry for the Age of the student/teacher
        entry_b.place(x=770, y=330)

        # Label for where the user enters their class
        label_c = tk.Label(self, text="Class", width=20, font=small_font)
        label_c.place(x=598, y=380)

        school_class = tk.StringVar()

        # Entry for the class in which the student/teacher is apart of
        entry_c = tk.Entry(self, textvariable=school_class)
        entry_c.place(x=770, y=380)

        # Where the user enters their gender
        label_2 = tk.Label(self, text="Gender", width=20, font=small_font)
        label_2.place(x=600, y=450)
        var = tk.IntVar()

        tk.Radiobutton(self, text="Male", padx=5, variable=var, value=1).place(
            x=735, y=450)  # The options for the user gender male
        tk.Radiobutton(self, text="Female", padx=20, variable=var, value=2).place(
            x=820, y=450)  # the options for the user gender female

        label_3 = tk.Label(self, text="School", width=20, font=small_font)  # School of the user
        label_3.place(x=600, y=520)

        var1 = tk.IntVar()
        tk.Radiobutton(self, text="Student", padx=5, variable=var1, value=1).place(
            x=735, y=520)  # Option for the user either student
        tk.Radiobutton(self, text="Teacher", padx=20, variable=var1, value=2).place(
            x=820, y=520)  # Option for the user either teacher
        button1 = tk.Button(self, text="Enter details",
                            command=lambda: controller.show_frame(Register2))  # Shows us traversal between the two buttons
        button1.place(x=900, y=600)


class Register2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Changes the background of the colour to be grey (allows for the specific frame to be styled)
        tk.Frame.config(self, bg="grey")
        # Title Page of the second part of the Registration Form
        label = tk.Label(self, text="Register 2", font=title_font, bg="grey")
        label.pack(pady=10, padx=10)

        # Label for where the user enters their username
        label_0 = tk.Label(self, text="Username", font=small_font, bg="grey")
        label_0.pack()

        username_entry = tk.StringVar()
        entry_0 = tk.Entry(self, textvariable=username_entry)
        entry_0.pack()

        # Label for where the user enters their username
        label_1 = tk.Label(self, text="Password", bg="grey")
        label_1.pack()

        password_entry = tk.StringVar()  # Stores the actual password the user password

        # Hides the user password when being typed in
        entry_1 = tk.Entry(self, textvariable=password_entry, show="*")
        entry_1.pack()

        # Label for where the user confirms the password they typed
        label_2 = tk.Label(self, text="Confirm Password", bg="grey")
        label_2.pack()

        password_confirm = tk.StringVar()  # Stores the actual password the user password again (used for comparison)

        # Hides the user password when being typed in
        entry_2 = tk.Entry(self, textvariable=password_confirm, show="*")
        entry_2.pack()

        # Label for where the user enters their email address
        label_3 = tk.Label(self, text="Email", bg="grey")
        label_3.pack()

        email_entry = tk.StringVar()
        entry_3 = tk.Entry(self, textvariable=email_entry)
        entry_3.pack()
        button1 = ttk.Button(self, text="Back to home",
                             command=lambda: controller.show_frame(Register))
        button1.pack()


root = MathsPro()  # this runs the Maths Pro class
root.geometry("1280x800")  # changes the size of the window
root.mainloop()  # As MathsPro inherited from tkinter this function can be moved
