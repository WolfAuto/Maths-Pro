import tkinter as tk
from tkinter import ttk
# this is import the functionailty of the registration from another python file
from remake_register import register1, register2
title_font = ("Times New Roman", 50)  # Setting font for titles on the frames
large_font = ("Times New Roman", 24)  # Setting fonts for main headings
medium_font = ("Times New Roman", 16)  # Setting fonts for text that will appear on the screen
small_font = ("Times New Roman", 12)  # Setting fonts for small deails to be displayed

# http://inloop.github.io/sqlite-viewer/ for checking the database file https://sqliteonline.com/


class MathsPro(tk.Tk):

    def __init__(self, *args, **kwargs):  # Creating a class that inherits from tk.Tk

        tk.Tk.__init__(self, *args, **kwargs)  # intialises the object
        self.shared_data = {"firstname": tk.StringVar(),  # dictionary that stores the user register information
                            "surname": tk.StringVar(),    # through using the controller we can pass these variables
                            "age": tk.StringVar(),        # to different frames
                            "Class": tk.StringVar(),
                            "var": tk.IntVar(),
                            "gender": tk.StringVar(),
                            "var1": tk.IntVar(),
                            "username": tk.StringVar(),
                            "password": tk.StringVar(),
                            "confirm_password": tk.StringVar(),
                            "email": tk.StringVar()}

        tk.Tk.wm_title(self, "Maths Pro")  # Sets the title of each page to be Maths Pro
        container = tk.Frame(self)  # defined a container for all the frame be kept

        # The containter is filled with a bunch of frames
        container.pack(side="top", fill="both", expand=True)
        # After the page being packed this allows it to be displayed correctly
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Empty dictionary where all the frames are kept
        # contains all the pages being used doesn't work without multiple frames (more than one)
        for F in (Register, Register2, Main_Menu):

            # Defines the frame from the for loop which contains all the pages
            frame = F(container, self)

            self.frames[F] = frame  # Sets the top frame to be the current frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.frames[F] = frame  # Sets the frame to be the value of the frame in the dictionary

        # This allows the frame to be displayed and streched
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Register2)  # sets the first frame to be shown is a register page

    def show_frame(self, cont):  # method that takes in cont as a controller

        frame = self.frames[cont]  # Defines the frame from the chosen frame in the dictionary
        frame.tkraise()  # Brings the frame to the top for the user to see


class Register(tk.Frame):  # Creating a class that inheirts tk.Frame from tkinter

    def __init__(self, parent, controller):  # intialise the class register with self, args and kwargs
        tk.Frame.__init__(self, parent)  # intialise the frame with self and parent class
        self.controller = controller  # Controlller functions to be used in different frames
        # tk.Frame.config(self) allows the frame to be styled i.e changing background colour
        # Title Page of the Registration Form
        title_label = tk.Label(self, text="Registration 1", font=title_font)
        title_label.grid(row=0, column=0)
        # Adds a separator between instructions and the registration form
        separator = ttk.Separator(self, orient="vertical")
        separator.grid(row=1, column=10, rowspan=7, sticky="ns")
        # Label giving instructions on what to do
        intro = (
            """Registration Page please enter your personal details\nand press the button to confirm your details""")
        intro_label = tk.Label(
            self, text=intro, font=small_font)
        intro_label.grid(row=3, column=11)

        # Label for where the user enters their first name
        firstname_label = tk.Label(self, text="First Name", font=small_font)
        firstname_label.grid(row=1, column=0, pady=20)

        # Where the user enter their first name and the variable it is stored in
        firstname_entry = tk.Entry(self, textvariable=self.controller.shared_data["firstname"])
        firstname_entry.grid(row=1, column=1)

        # Label for where the user enters their surname
        surname_label = tk.Label(self, text="Surname", font=small_font)
        surname_label.grid(row=2, column=0, pady=20)

        # Entry of the surname of user and the variable it is stored in
        surname_entry = tk.Entry(self, textvariable=self.controller.shared_data["surname"])
        surname_entry.grid(row=2, column=1)

        # Label for where the user enters their age
        age_label = tk.Label(self, text="Age", font=small_font)
        age_label.grid(row=3, column=0, pady=20)

        # Entry for the Age of the student/teacher and the variable it is stored in
        age_entry = tk.Entry(self, textvariable=self.controller.shared_data["age"])
        age_entry.grid(row=3, column=1)

        # Label for where the user enters their class
        class_label = tk.Label(self, text="Class", font=small_font)
        class_label.grid(row=4, column=0, pady=20)

        # Entry for the class in which the student/teacher is apart of and the variable it is stored in
        all_classes = ["12C", "12D", "13C", "13D"]
        droplist = tk.OptionMenu(self, self.controller.shared_data["Class"], *all_classes)
        droplist.config(width=20)
        self.controller.shared_data["Class"].set("Select your class")
        droplist.grid(row=4, column=1)

        # Where the user enters their gender
        gender_label = tk.Label(self, text="Gender", font=small_font)
        gender_label.grid(row=5, column=0, pady=20)

        # Using tkinter radiobuttons to make check box for gender
        tk.Radiobutton(self, text="Male", padx=5, variable=self.controller.shared_data["var"], value=1).grid(
            row=5, column=1)  # The options for the user gender value 1 (male) and the variable it is stored in
        tk.Radiobutton(self, text="Female", padx=20, variable=self.controller.shared_data["var"], value=2).grid(
            row=5, column=2)  # the options for the user gender value 2 (female) and the variable it is stored in

        # Label for where the user enters whether they are student or teacher
        school_label = tk.Label(self, text="School", width=20,
                                font=small_font)
        school_label.grid(row=6, column=0, pady=20)

        # Using tkinter radiobuttons to make a check box for student or teacher
        tk.Radiobutton(self, text="Student", padx=5, variable=self.controller.shared_data["var1"], value=1).grid(
            row=6, column=1)  # Option for the user either value 1 (student) and the variable it is stored in
        tk.Radiobutton(self, text="Teacher", padx=20, variable=self.controller.shared_data["var1"], value=2).grid(
            row=6, column=2)  # Option for the user either value 2 (teacher) and the variable it is stored in
        # Enters all the user information using the register function from the other python file

        # Stores the image of the button
        photo = tk.PhotoImage(file="button.png")
        # Creates the button with the image stored
        help_button = tk.Button(self, text="Help Button", image=photo)
        # Removes the border on the button
        help_button.config(border="0")
        # Places the button in the bottom left corner
        help_button.place(x=0, y=730)
        # Sets the image of the button to be the photo
        help_button.image = photo
        # Alllows the user to go back to previous screen
        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(Main_Menu))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)
        # Terminates the whole program
        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)
        enter_details = tk.Button(self, text="Enter details",
                                  command=lambda: self.register(self.controller, self.controller.shared_data["firstname"].get(),
                                                                self.controller.shared_data["surname"].get(
                                  ),
                                      self.controller.shared_data["age"].get(
                                  ),
                                      self.controller.shared_data["Class"].get(
                                  ),
                                      self.controller.shared_data["var"].get(
                                  ),
                                      self.controller.shared_data["var1"].get()))
        enter_details.grid(row=7, column=9)

    def register(self, controller, firstname, surname, age, school_class, var, var1):  # function used changing frames
        # vaildation of all the personal deatils and these details being added into the record
        if register1(firstname, surname, age, school_class, var, var1) is True:
            controller.show_frame(Register2)
        # elif register1(firstname, surname, age, school_class, var, var1) == pass:
        #    controller.show_frame(Register2)  # switches to the next part of the registration


class Register2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Changes the background of the colour to be grey (allows for the specific frame to be styled)
        tk.Frame.config(self, bg="grey")
        self.controller = controller
        # Title Page of the second part of the Registration Form
        label = tk.Label(self, text="Register 2", font=title_font, bg="grey")
        label.grid(row=0, column=0)
        # Adds a separator between the form and instruction text
        separator = ttk.Separator(self, orient="vertical")
        separator.grid(row=1, column=3, rowspan=7, sticky="ns")
        # instruction text for username and password
        guide = ("Enter a username 6 or more characters long and password that is 8 characters long"
                 + "\n" + "contains uppercase, lowercase, digits and special characters")
        label_text = tk.Label(self, text=guide, font=small_font, bg="grey")
        label_text.grid(row=2, column=4)

        # Label for where the user enters their username
        username_label = tk.Label(self, text="Username", font=small_font, bg="grey")
        username_label.grid(row=1, column=0, pady=20)
        # Entry for username and the variable it is stored in
        username_entry = tk.Entry(self, textvariable=self.controller.shared_data["username"])
        username_entry.grid(row=1, column=1)

        # Label for where the user enters their username
        password_label = tk.Label(self, text="Password", bg="grey")
        password_label.grid(row=2, column=0, pady=20)

        # Hides the user password when being typed in and takes in the user input for password
        password_entry = tk.Entry(
            self, textvariable=self.controller.shared_data["password"], show="*")
        password_entry.grid(row=2, column=1)

        # Label for where the user confirms the password they typed
        confirm_label = tk.Label(self, text="Confirm Password", bg="grey")
        confirm_label.grid(row=3, column=0, pady=20)

        # Hides the user password when being typed in and takes in the user input for password second time
        confirm_entry = tk.Entry(
            self, textvariable=self.controller.shared_data["confirm_password"], show="*")
        confirm_entry.grid(row=3, column=1)

        # Label for where the user enters their email address
        email_label = tk.Label(self, text="Email", bg="grey")
        email_label.grid(row=4, column=0, pady=20)
        # Entry for email and the variable it is stored in
        email_entry = tk.Entry(self, textvariable=self.controller.shared_data["email"])
        email_entry.grid(row=4, column=1)

        # Stores the image of the button
        photo = tk.PhotoImage(file="button.png")
        # Creates the button with the image stored
        help_button = tk.Button(self, text="Help Button", image=photo)
        # Removes the border on the button
        help_button.config(border="0",  bg="grey")
        # Places the button in the bottom left corner
        help_button.place(x=0, y=730)
        # Sets the image of the button to be the photo
        help_button.image = photo
        # Terminates the whole program
        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)
        # Alllows the user to go back to previous screen
        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(Register))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)
        # Creates account and emails the user
        create_button = ttk.Button(self, text="Create Account", command=lambda: self.register(
            self.controller,
            self.controller.shared_data["username"].get(
            ), self.controller.shared_data["password"].get(),
            self.controller.shared_data["confirm_password"].get(
            ), self.controller.shared_data["email"].get(),
            self.controller.shared_data["var1"].get()))
        create_button.grid(row=6, column=2)

    def register(self, controller, username, password, password_confirm, email, var1):
        if register2(username, password, password_confirm, email, var1) is True:
            controller.show_frame(Main_Menu)


class Main_Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="blue")
        # Title of Main Menu
        title_label = tk.Label(self, text="Maths Pro", font=title_font)
        title_label.pack(padx=20, pady=20)
        # Label of username
        username_label = tk.Label(self, text="Username", font=medium_font)
        username_label.pack()
        # Stores the value of the username
        username = tk.StringVar()
        # Entry of the username and the variable it is stored in
        username_entry = tk.Entry(self, textvariable=username)
        username_entry.pack()
        # Label of password
        password_label = tk.Label(self, text="Password", font=medium_font)
        password_label.pack()
        # Stores what the user types in
        password = tk.StringVar()
        # Entry of the password, hide what the user types in and the variable  it is stored in
        password_entry = tk.Entry(self, textvariable=password, show="*")
        password_entry.pack()

        # Stores the image of the button
        photo = tk.PhotoImage(file="button.png")
        # Creates the button with the image stored
        help_button = tk.Button(self, text="Help Button", image=photo)
        # Removes the border on the button
        help_button.config(border="0")
        # Places the button in the bottom left corner
        help_button.place(x=0, y=730)
        # Sets the image of the button to be the photo
        help_button.image = photo

        # Terminates the whole program
        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)


root = MathsPro()  # this runs the Maths Pro class
root.geometry("1280x800")  # changes the size of the window
root.resizable(width=False, height=False)  # Prevents the root size from being changed
root.mainloop()  # As MathsPro inherited from tkinter this function can be moved
