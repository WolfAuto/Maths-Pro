import tkinter as tk
from tkinter import ttk
from login_backend import login_in
from tkinter import messagebox
title_font = ("Times New Roman", 50)
medium_font = ("Times New Roman", 26)


class MathsPro(tk.Tk):  # Creating a class that inherits from tk.Tk

    def __init__(self, *args, **kwargs):  # intialises the object
        # intialises the object as a tkinter frame
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="")
        # Sets the title of each page to be Maths Pro
        tk.Tk.wm_title(self, "Maths Pro")
        # defined a container for all the framesto be kept
        container = tk.Frame(self)

        # The containter is filled with a bunch of frames
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        # After the page being packed this allows it to be displayed correctly
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Empty dictionary where all the frames are kept

        # contains all the pages being used #this will not work without pages
        for F in (Main_Menu, StudentArea, TeacherArea):

            # Defines the frame from the for loop which contains all the pages
            frame = F(container, self)

            # Sets the top frame to be the current frame
            self.frames[F] = frame

            # This allows the frame to be displayed and streched
            frame.grid(row=0, column=0, sticky="nsew")

        # sets the first frame to be shown is a register page
        self.show_frame(Main_Menu)

    def show_frame(self, cont):  # method that takes in cont as a controller

        # Defines the frame from the chosen frame in the dictionary
        frame = self.frames[cont]
        frame.tkraise()  # Brings the frame to the top for the user to see


class Main_Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Maths Pro", bg="blue", font=title_font)
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

        button = ttk.Button(self, text="Login", command=lambda: self.vaildate(
            controller, username_entry.get(), password_entry.get()))
        button.pack()

        button1 = ttk.Button(self, text="Student Area",
                             command=lambda: controller.show_frame(StudentArea))
        button1.pack()

        button2 = ttk.Button(self, text="Teacher Area",
                             command=lambda: controller.show_frame(TeacherArea))
        button2.pack()

        photo = tk.PhotoImage(file="button.png")
        help_button = tk.Button(self, text="Help Button", image=photo)
        help_button.config(border="0")
        help_button.place(x=0, y=730)

        help_button.image = photo
        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)

        login_button = tk.Button(
            self, text="Login", command=lambda: self.vaildate(controller, username_entry.get(), password_entry.get()))
        login_button.config(bg="blue", fg="green")
        login_button.place(x=400, y=300)

    def vaildate(self, controller, username, password):
        if login_in(username, password) == "S":
            controller.show_frame(StudentArea)
       if login_in(username, password) == "T":
            controller.show_frame(TeacherArea)
        else:
            messagebox.showwarning("Account", "Account doesn't exist")


class StudentArea(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        label = tk.Label(self, text="Student Area", font=title_font)
        label.config(bg="blue", fg="white")
        label.pack(pady=10, padx=10, side="top", anchor="nw")

        teacher_button = tk.Button(self, text="Teacher Area",
                                   command=lambda: controller.show_frame(TeacherArea))
        teacher_button.pack(side="right", anchor="e")

        info_text = tk.Label(
            self, text="Welcome Student please choose from the following", font=medium_font, bg="grey")
        info_text.place(x=350, y=100)
        account_button = tk.Button(self, text="View Account Infomation")
        account_button.config(height=5, width=30, bg="blue")
        account_button.place(x=400, y=450)

        info_button = tk.Button(self, text="View Maths Information")
        info_button.config(height=5, width=30, bg="blue")
        info_button.place(x=750, y=450)

        math_button1 = tk.Button(self, text="AS Maths")
        math_button1.config(height=5, width=30, bg="blue")
        math_button1.place(x=400, y=250)

        math_button2 = tk.Button(self, text="A2 Maths")
        math_button2.config(height=5, width=30, bg="blue")
        math_button2.place(x=750, y=250)

        help_button = tk.Button(self, text="Help Button")
        help_button.config(height=3, width=10, bg="blue")
        help_button.place(x=0, y=750)

        logout_button = tk.Button(self, text="Log out",
                                  command=lambda: controller.show_frame(Main_Menu))
        logout_button.config(height=3, width=10, bg="blue", fg="white")
        logout_button.place(x=1050, y=750)

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(height=3, width=10, bg="blue")
        quit_button.place(x=1200, y=750)


class TeacherArea(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        label_text = tk.Label(self, text="Teacher Area", font=title_font)
        label_text.config(bg="blue", fg="white")
        label_text.pack(pady=10, padx=10, anchor="nw")
        info_text = tk.Label(
            self, text="Welcome Teacher please choose from the following", font=medium_font, bg="grey")
        info_text.place(x=350, y=100)

        button1 = tk.Button(self, text="Student Area",
                            command=lambda: controller.show_frame(StudentArea))
        button1.pack()

        button2 = tk.Button(self, text="View Account Information")
        button2.config(height=5, width=30, bg="blue", fg="white")
        button2.place(x=750, y=450)

        button3 = tk.Button(self, text="View Student/Class Information")
        button3.place(x=400, y=250)
        button3.config(height=5, width=30, bg="blue", fg="white")

        button4 = tk.Button(self, text="View Flagged Students")
        button4.place(x=750, y=250)
        button4.config(height=5, width=30, bg="blue", fg="white")

        button5 = tk.Button(self, text="Set Test Date")
        button5.place(x=400, y=450)
        button5.config(height=5, width=30, bg="blue", fg="white")

        help_button = tk.Button(self, text="Help Button")
        help_button.config(height=3, width=10, bg="blue", fg="white")
        help_button.place(x=0, y=750)

        logout_button = tk.Button(self, text="Log out",
                                  command=lambda: controller.show_frame(Main_Menu))
        logout_button.config(height=3, width=10, bg="blue", fg="white")
        logout_button.place(x=1050, y=750)

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)


root = MathsPro()  # this runs the Maths Pro class
root.geometry("1280x800")  # changes the size of the window
root.resizable(width=False, height=False)
root.mainloop()  # As MathsPro inherited from tkinter this function can be moved
