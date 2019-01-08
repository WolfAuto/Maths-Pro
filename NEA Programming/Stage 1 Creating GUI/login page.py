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

        # contains all the pages being used #this will not work without pages
        for F in (MainMenu, StudentArea, TeacherArea):

            # Defines the frame from the for loop which contains all the pages
            frame = F(container, self)

            self.frames[F] = frame  # Sets the top frame to be the current frame

            # This allows the frame to be displayed and streched
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)  # sets the first frame to be shown is a register page

    def show_frame(self, cont):  # method that takes in cont as a controller

        frame = self.frames[cont]  # Defines the frame from the chosen frame in the dictionary
        frame.tkraise()  # Brings the frame to the top for the user to see


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Maths Pro", bg="blue")
        label.pack(pady=10, padx=10)

        label_1 = tk.Label(self, text="Username")
        label_1.pack()

        username_entry = tk.StringVar()
        entry_1 = tk.Entry(self, textvariable=username_entry)
        entry_1.pack()

        label_2 = tk.Label(self, text="Password")
        label_2.pack()

        password_entry = tk.StringVar()
        entry_2 = tk.Entry(self, textvariable=password_entry)
        entry_2.pack()

        button = ttk.Button(self, text="Login")
        button.pack()



        button1 = ttk.Button(self, text="Student Area",
                            command=lambda: controller.show_frame(StudentArea))
        button1.pack()

        button2 = ttk.Button(self, text="Teacher Area",
                             command=lambda: controller.show_frame(TeacherArea))
        button2.pack()


class StudentArea(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        label = tk.Label(self, text="Student Area")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Log out", command=lambda: controller.show_frame(MainMenu))
        button.pack()

        button1 = ttk.Button(self, text="Teacher Area",
                             command=lambda: controller.show_frame(TeacherArea))
        button1.pack()


class TeacherArea(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        label = tk.Label(self, text="Teacher Area")
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Log out", command=lambda: controller.show_frame(MainMenu))
        button1.pack()

        button1 = ttk.Button(self, text="Student Area",
                             command=lambda: controller.show_frame(StudentArea))
        button1.pack()


root = MathsPro()  # this runs the Maths Pro class
root.geometry("1280x800")  # changes the size of the window
root.mainloop()  # As MathsPro inherited from tkinter this function can be moved
