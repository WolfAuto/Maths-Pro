import tkinter as tk
import tkinter.scrolledtext as tkst
import re
from tkinter import ttk
from tkinter import messagebox
from matplotlib.pyplot import close as end
# this is import the functionailty of the registration from another python file
from remake_register import register1, register2
from test_dates import set_test, show_details
from login_backend import login_in, forgot_password, support_email, back_button, get_id_student
from questions_results import make_question, get_question, compare_answers, end_loop
from creating_graphs import correct_graphs,incorrect_graphs,total_graph_correct, total_graph_incorrect,graph_total_questions,score_graph,total_score

import view_account as va
import student_class as sc

title_font = ("Times New Roman", 50)  # Setting font for titles on the frames
large_font = ("Times New Roman", 30)  # Setting fonts for main headings
medium_font = ("Times New Roman", 16)  # Setting fonts for text that will appear on the screen
small_font = ("Times New Roman", 12)  # Setting fonts for small deails to be displayed


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
                            "email": tk.StringVar(),
                            "login_username": "blank",
                            "School": "blank",
                            "header": None,
                            "details": None,
                            "date": tk.StringVar(),
                            "var_type": tk.IntVar(),
                            "var_level": tk.IntVar(),
                            "comments": tk.StringVar(),
                            "test_type": tk.IntVar(),
                            "test_level": tk.StringVar(),
                            "type": tk.IntVar(),
                            "level": tk.IntVar(),
                            "answer": tk.StringVar(),
                            "Loop": tk.StringVar(),
                            "Loop_type": tk.StringVar(),
                            "student_id": 0}

        tk.Tk.wm_title(self, "Maths Pro")  # Sets the title of each page to be Maths Pro
        container = tk.Frame(self)  # defined a container for all the frame be kept

        # The containter is filled with a bunch of frames
        container.pack(side="top", fill="both", expand=True)
        # After the page being packed this allows it to be displayed correctly
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Empty dictionary where all the frames are kept
        # contains all the pages being used doesn't work without multiple frames (more than one)
        for F in (Main_Menu, Register, Register2, StudentArea, TeacherArea, Help_Page, ViewAccountInfo, SetTestDate, entry_questions, StudentandClass, Add_Question, Question_Loop, MathsInfo):

            # Defines the frame from the for loop which contains all the pages
            frame = F(container, self)

            self.frames[F] = frame  # Sets the top frame to be the current frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.frames[F] = frame  # Sets the frame to be the value of the frame in the dictionary

        # This allows the frame to be displayed and streched
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main_Menu)  # sets the first frame to be shown is a register page

    def get_page(self, page_class):
        return self.frames[page_class]

    def show_frame(self, cont):  # method that takes in cont as a controller

        frame = self.frames[cont]  # Defines the frame from the chosen frame in the dictionary
        frame.tkraise()  # Brings the frame to the top for the user to see
        frame.update() # updates what pointer the frame is looking at
        frame.event_generate("<<ShowFrame>>") # causes an event to occur when a frame is is shown

    def update_widgets(self, frame_list, widget_name, criteria, output):
        for i in frame_list:
            frame = self.frames[i]
            label = getattr(frame, widget_name)
            label[criteria] = output


class Main_Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        title_label = tk.Label(self, text="Maths Pro", bg="blue", fg="white", font=title_font)
        title_label.pack(pady=10, padx=10, fill="x")
        self.bind("<<ShowFrame>>", self.on_show_frame)
        welcome = (
            "Welcome to Maths Pro please Login in if you alredy have an account or Register if you don't have an account")
        welcome_label = tk.Label(self, text=welcome, font=small_font)
        welcome_label.place(x=360, y=610)

        pic1 = tk.PhotoImage(file="pic1.png")
        pic2 = tk.PhotoImage(file="pic3.gif")

        picture1 = tk.Label(self, image=pic1)
        picture1.config(border="0")
        picture1.place(x=70, y=250)
        picture1.image = pic1

        picture2 = tk.Label(self, image=pic2)
        picture2.config(border="0")
        picture2.place(x=850, y=220)
        picture2.image = pic2

        username_label = tk.Label(self, text="Username", font=medium_font)
        username_label.place(x=410, y=230)

        username_entry = tk.StringVar()
        username_box = tk.Entry(self, textvariable=username_entry)
        username_box.place(x=610, y=240)

        password_label = tk.Label(self, text="Password", font=medium_font)
        password_label.place(x=410, y=330)

        password_entry = tk.StringVar()
        password_box = tk.Entry(self, textvariable=password_entry, show="*")
        password_box.place(x=610, y=340)

        login_button = tk.Button(self, text="Login", command=lambda: [self.vaildate(
            controller, username_entry.get(), password_entry.get()), username_box.delete(0, tk.END), password_box.delete(0, tk.END)])
        login_button.config(height=3, width=15, bg="blue", fg="white")
        login_button.place(x=370, y=420)

        register_button = tk.Button(self, text="Register",
                                    command=lambda: controller.show_frame(Register))
        register_button.config(height=3, width=15, bg="blue", fg="white")
        register_button.place(x=720, y=420)

        photo = tk.PhotoImage(file="button.png")
        help_button = tk.Button(self, image=photo,
                                command=lambda: controller.show_frame(Help_Page))
        help_button.config(border="0")
        help_button.place(x=0, y=730)
        help_button.image = photo

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)

    def vaildate(self, controller, username, password):
        if login_in(username, password) == "S":
            controller.show_frame(StudentArea)
            self.controller.shared_data["login_username"] = username
            self.controller.shared_data["School"] = "Student"
            self.controller.shared_data["student_id"] = get_id_student(username)
            print(self.controller.shared_data["student_id"])
        elif login_in(username, password) == "T":
            controller.show_frame(TeacherArea)
            self.controller.shared_data["login_username"] = username
            self.controller.shared_data["School"] = "Teacher"
        else:
            messagebox.showwarning("Account", "Account doesn't exist")
    def on_show_frame(self,event):
        self.controller.shared_data["login_username"] ="blank"
        self.controller.shared_data["School"] = "blank"


class Register(tk.Frame):  # Creating a class that inheirts tk.Frame from tkinter

    def __init__(self, parent, controller):  # intialise the class register with self, args and kwargs
        tk.Frame.__init__(self, parent)  # intialise the frame with self and parent class
        tk.Frame.config(self, bg="grey")
        self.controller = controller  # Controlller functions to be used in different frames
        # tk.Frame.config(self) allows the frame to be styled i.e changing background colour
        # Title Page of the Registration Form
        title_label = tk.Label(self, text="Registration 1", font=title_font, bg="grey")
        title_label.grid(row=0, column=0)
        # Adds a separator between instructions and the registration form
        separator = ttk.Separator(self, orient="vertical")
        separator.grid(row=1, column=10, rowspan=7, sticky="ns")
        # Label giving instructions on what to do
        intro = (
            """Registration Page please enter your personal details\nandpress the button to confirm your details please enter a captial letter for your frstname and surname""")
        intro_label = tk.Label(
            self, text=intro, font=small_font, bg="grey")
        intro_label.grid(row=3, column=11)

        # Label for where the user enters their first name
        firstname_label = tk.Label(self, text="First Name", font=small_font, bg="grey")
        firstname_label.grid(row=1, column=0, pady=20)

        # Where the user enter their first name and the variable it is stored in
        firstname_entry = tk.Entry(self, textvariable=self.controller.shared_data["firstname"])
        firstname_entry.grid(row=1, column=1)

        # Label for where the user enters their surname
        surname_label = tk.Label(self, text="Surname", font=small_font, bg="grey")
        surname_label.grid(row=2, column=0, pady=20)

        # Entry of the surname of user and the variable it is stored in
        surname_entry = tk.Entry(self, textvariable=self.controller.shared_data["surname"])
        surname_entry.grid(row=2, column=1)

        # Label for where the user enters their age
        age_label = tk.Label(self, text="Age", font=small_font, bg="grey")
        age_label.grid(row=3, column=0, pady=20)

        # Entry for the Age of the student/teacher and the variable it is stored in
        age_entry = tk.Entry(self, textvariable=self.controller.shared_data["age"])
        age_entry.grid(row=3, column=1)

        # Label for where the user enters their class
        class_label = tk.Label(self, text="Class", font=small_font, bg="grey")
        class_label.grid(row=4, column=0, pady=20)

        # Entry for the class in which the student/teacher is apart of and the variable it is stored in
        all_classes = ["12C", "12D", "13C", "13D"]
        droplist = tk.OptionMenu(self, self.controller.shared_data["Class"], *all_classes)
        droplist.config(width=20, border="0")
        self.controller.shared_data["Class"].set("Select your class")
        droplist.grid(row=4, column=1)

        # Where the user enters their gender
        gender_label = tk.Label(self, text="Gender", font=small_font, bg="grey")
        gender_label.grid(row=5, column=0, pady=20)

        # Using tkinter radiobuttons to make check box for gender
        tk.Radiobutton(self, text="Male", padx=5, variable=self.controller.shared_data["var"], value=1, bg="grey").grid(
            row=5, column=1)  # The options for the user gender value 1 (male) and the variable it is stored in
        tk.Radiobutton(self, text="Female", padx=20, variable=self.controller.shared_data["var"], value=2, bg="grey").grid(
            row=5, column=2)  # the options for the user gender value 2 (female) and the variable it is stored in

        # Label for where the user enters whether they are student or teacher
        school_label = tk.Label(self, text="School", width=20,
                                font=small_font, bg="grey")
        school_label.grid(row=6, column=0, pady=20)

        # Using tkinter radiobuttons to make a check box for student or teacher
        tk.Radiobutton(self, text="Student", padx=5, variable=self.controller.shared_data["var1"], value=1, bg="grey").grid(
            row=6, column=1)  # Option for the user either value 1 (student) and the variable it is stored in
        tk.Radiobutton(self, text="Teacher", padx=20, variable=self.controller.shared_data["var1"], value=2, bg="grey").grid(
            row=6, column=2)  # Option for the user either value 2 (teacher) and the variable it is stored in

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(Main_Menu))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)
        # Terminates the whole program
        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)
        # Enters all the user information using the register function from the other python file
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
        enter_details.config(height=3, width=10, bg="blue", fg="white")
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

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)
        # Alllows the user to go back to previous screen
        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(Register))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)
        # Creates account and emails the user
        create_button = tk.Button(self, text="Create Account", command=lambda: self.register(
            self.controller,
            self.controller.shared_data["username"].get(
            ), self.controller.shared_data["password"].get(),
            self.controller.shared_data["confirm_password"].get(
            ), self.controller.shared_data["email"].get(),
            self.controller.shared_data["var1"].get()))
        create_button.config(height=3, width=12, bg="blue", fg="white")
        create_button.grid(row=6, column=2)

    def register(self, controller, username, password, password_confirm, email, var1): #function that calls the register function in the backend
        if register2(username, password, password_confirm, email, var1) is True: # if register2 has been fully completed
            controller.show_frame(Main_Menu) # shows the Main_Menu page
            messagebox.showinfo(
                "Account Creation", "Account creation has been successful an email has been sent to you") # displays a tkinter info message


class StudentArea(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        self.controller = controller

        label = tk.Label(self, text="Student Area", font=title_font)
        label.config(bg="blue", fg="white")
        label.pack(pady=10, padx=10, side="top", anchor="nw")

        info_text = tk.Label(
            self, text="Welcome Student please choose from the following", font=medium_font, bg="grey")
        info_text.place(x=350, y=100)
        account_button = tk.Button(self, text="View Account Infomation",
                                   command=lambda: [self.update_labels(),
                                                    controller.show_frame(ViewAccountInfo)])
        account_button.config(height=5, width=30, bg="blue", fg="white")
        account_button.place(x=400, y=450)

        info_button = tk.Button(self, text="View Maths Information", command=lambda: [
                                self.score_label(), controller.show_frame(MathsInfo)])
        info_button.config(height=5, width=30, bg="blue", fg="white")
        info_button.place(x=750, y=450)

        math_button1 = tk.Button(self, text="AS Maths", command=lambda: [
                                 controller.show_frame(entry_questions), self.change_AS()])
        math_button1.config(height=5, width=30, bg="blue", fg="white")
        math_button1.place(x=400, y=250)

        math_button2 = tk.Button(self, text="A2 Maths", command=lambda: [
                                 controller.show_frame(entry_questions), self.change_A2()])
        math_button2.config(height=5, width=30, bg="blue", fg="white")
        math_button2.place(x=750, y=250)

        photo = tk.PhotoImage(file="button.png")
        help_button = tk.Button(self, text="Help Button", image=photo,
                                command=lambda: controller.show_frame(Help_Page))
        help_button.config(border="0", bg="grey")
        help_button.place(x=0, y=730)
        help_button.image = photo

        logout_button = tk.Button(self, text="Log out",
                                  command=lambda: controller.show_frame(Main_Menu))
                                                                                                        
        logout_button.config(height=3, width=10, bg="blue", fg="white")
        logout_button.place(x=1050, y=750)

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(height=3, width=10, bg="blue", fg="white")
        quit_button.place(x=1200, y=750)

        test_button = tk.Button(self, text="Show Tests", command=lambda: show_details())
        test_button.config(height=3, width=10, bg="blue", fg="white")
        test_button.place(x=100, y=650)

    def update_labels(self):
        va.view_info(self.controller.shared_data["login_username"],
                     self.controller.shared_data["School"])
        self.controller.update_widgets(
            [ViewAccountInfo], "header", "text", va.header)
        self.controller.update_widgets(
            [ViewAccountInfo], "result", "text", va.result)

    def change_AS(self):
        self.controller.shared_data["test_level"] = "AS"

    def change_A2(self):
        self.controller.shared_data["test_level"] = "A2"

    def score_label(self):
        self.controller.update_widgets([MathsInfo], "score_result","text",total_score(
            self.controller.shared_data["student_id"]))


class TeacherArea(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        self.controller = controller
        label_text = tk.Label(self, text="Teacher Area", font=title_font)
        label_text.config(bg="blue", fg="white")
        label_text.pack(pady=10, padx=10, anchor="nw")
        info_text = tk.Label(
            self, text="Welcome Teacher please choose from the following", font=medium_font, bg="grey")
        info_text.place(x=350, y=100)

        account_info = tk.Button(self, text="View Account Information",
                                 command=lambda: [controller.show_frame(ViewAccountInfo), self.update_labels()])
        account_info.config(height=5, width=30, bg="blue", fg="white")
        account_info.place(x=750, y=450)

        student_class_information = tk.Button(
            self, text="View Student/Class Information", command=lambda: controller.show_frame(StudentandClass))
        student_class_information.place(x=400, y=250)
        student_class_information.config(height=5, width=30, bg="blue", fg="white")

        flagged_students = tk.Button(self, text="Add Question",
                                     command=lambda: controller.show_frame(Add_Question))
        flagged_students.place(x=750, y=250)
        flagged_students.config(height=5, width=30, bg="blue", fg="white")

        test_date = tk.Button(self, text="Set Test Date",
                              command=lambda: controller.show_frame(SetTestDate))
        test_date.place(x=400, y=450)
        test_date.config(height=5, width=30, bg="blue", fg="white")

        photo = tk.PhotoImage(file="button.png")
        help_button = tk.Button(self, text="Help Button", image=photo,
                                command=lambda: controller.show_frame(Help_Page))
        help_button.config(border="0", bg="grey")
        help_button.place(x=0, y=730)
        help_button.image = photo

        logout_button = tk.Button(self, text="Log out",
                                  command=lambda: controller.show_frame(Main_Menu))
        logout_button.config(height=3, width=10, bg="blue", fg="white")
        logout_button.place(x=1050, y=750)

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)

    def update_labels(self):
        va.view_info(self.controller.shared_data["login_username"],
                     self.controller.shared_data["School"])
        self.controller.update_widgets(
            [ViewAccountInfo], "header", "text", va.header)
        self.controller.update_widgets(
            [ViewAccountInfo], "result", "text", va.result)


class Help_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="cyan")
        self.controller = controller

        label = tk.Label(self, text="Help Page", font=title_font)
        label.config(bg="cyan")
        label.pack(pady=10, padx=10, side="top", anchor="nw")

        def toggle():
            if label_1.invisible: # makes the label disppear if invisible is true
                label_1.place_forget()
            else:
                label_1.place(x=300, y=110) # places the label if invisible is false
            label_1.invisible = not(label_1.invisible) # reverses the current boolean value of label.insvisible
            # if true then it becomes false or visa versa 
        def toggle1():
            if label_2.invisible:
                label_2.place_forget()
            else:
                label_2.place(x=250, y=210)
            label_2.invisible = not(label_2.invisible)

        def toggle2():
            if label_3.invisible:
                label_3.place_forget()
            else:
                label_3.place(x=250, y=310)
            label_3.invisible = not(label_3.invisible)

        def toggle3():
            if label_4.invisible:
                label_4.place_forget()
            else:
                label_4.place(x=300, y=405)
            label_4.invisible = not(label_4.invisible)

        def toggle4():
            if label_5.invisible:
                label_5.place_forget()
            else:
                label_5.place(x=300, y=505)
            label_5.invisible = not(label_5.invisible)

        def toggle5():
            if label_6.invisible:
                label_6.place_forget()
            else:
                label_6.place(x=250, y=610)
            label_6.invisible = not(label_6.invisible)
        help_button1 = tk.Button(self, text="What is Maths Pro?", command=toggle)
        help_button1.config(fg="white", bg="blue", height=3)
        help_button1.place(x=150, y=105)
        label_1 = tk.Label(
            self, text="Maths Pro is a revision app around maths \n that allows for continuous revision on A level Maths"
            ,bg="cyan", font=small_font)
        label_1.invisible = False

        help_button2 = tk.Button(self, text="Questions", command=toggle1)
        help_button2.config(fg="white", bg="blue", height=3, width=10)
        help_button2.place(x=150, y=205)
        label_2 = tk.Label(
            self, text="Questions are past paper questions from the Edexcel Exam board \n and are separated into AS and A2 as well as Pure and Appiled", bg="cyan", font=small_font)
        label_2.invisible = False

        help_button3 = tk.Button(self, text="Students Tests", command=toggle2)
        help_button3.config(fg="white", bg="blue", height=3)
        help_button3.place(x=150, y=300)
        label_3 = tk.Label(
            self, text="Remember you can see upcoming tests so be sure to revise for the test using maths pro", bg="cyan", font=small_font)
        label_3.invisible = False

        help_button4 = tk.Button(self, text="Teachers information", command=toggle3)
        help_button4.config(fg="white", bg="blue", height=3)
        help_button4.place(x=150, y=400)
        label_4 = tk.Label(
            self, text="You can access student information at any time using the view student button. \n please note there is no communication method between student and teacher", bg="cyan", font=small_font)
        label_4.invisible = False

        help_button5 = tk.Button(self, text="Student extra information", command=toggle4)
        help_button5.config(fg="white", bg="blue", height=3)
        help_button5.place(x=150, y=500)
        label_5 = tk.Label(
            self, text="Speak to your teacher about questions that you get \n wrong frequently as Maths Pro is about improvement", bg="cyan", font=small_font)
        label_5.invisible = False

        help_button6 = tk.Button(self, text="Further Maths", command=toggle5)
        help_button6.config(fg="white", bg="blue", height=3)
        help_button6.place(x=150, y=600)
        label_6 = tk.Label(
            self, text="Sadly maths pro doesn't have Further Maths Support this will be a Future update", bg="cyan", font=small_font)
        label_6.invisible = False

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(Main_Menu))
        back_button.config(height=3, width=10, bg="blue")
        back_button.place(x=1050, y=750)
        support_text = (
            "If you still have problems or which to recommend any updates you can email Maths Pro \n using the button below leave your name if you want follow up help")
        support_label = tk.Label(self, text=support_text, font=small_font)
        support_label.config(bg="cyan")
        support_label.place(x=700, y=150)

        support_button = tk.Button(self, text="Support", command=lambda: self.email_support())
        support_button.config(fg="white", bg="blue", height=3, width=15)
        support_button.place(x=870, y=200)

        form_text = ("Use the feature below to change your password if forgotten ")
        password_label = tk.Label(self, text=form_text, bg="cyan")
        password_label.place(x=870, y=270)
        email_label = tk.Label(self, text="Email Address", bg="cyan")
        email_label.place(x=870, y=320)

        email_input = tk.StringVar()
        email_entry = tk.Entry(self, textvariable=email_input)
        email_entry.place(x=1000, y=320)

        password_label = tk.Label(self, text="New Password", bg="cyan")
        password_label.place(x=870, y=420)
        password_input = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=password_input, show="*")
        password_entry.place(x=1000, y=420)

        confirm_label = tk.Label(self, text="Confirm New Password", bg="cyan")
        confirm_label.place(x=850, y=520)
        confirm_input = tk.StringVar()
        confirm_entry = tk.Entry(self, textvariable=confirm_input, show="*")
        confirm_entry.place(x=1000, y=520)

        enter_button = tk.Button(self, text="Enter details", bg="blue", fg="white", command=lambda: [self.change_password(email_input.get(
        ), password_input.get(), confirm_input.get()), email_entry.delete(0, tk.END), password_entry.delete(0, tk.END), confirm_entry.delete(0, tk.END)])
        enter_button.config(height=3, width=10)
        enter_button.place(x=890, y=600)

        back_button = tk.Button(self, text="Back",
                                command=lambda: self.changing_frames(controller, self.controller.shared_data["School"]))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)

    def change_password(self, email, new_pass, confirm_pass):
        if forgot_password(email, new_pass, confirm_pass) is True:
            messagebox.showinfo("Password", "Password has been changed")

    def email_support(self):
        if support_email() is True:
            messagebox.showinfo("Support Email", "The email you have made has been sent to support")

    def changing_frames(self, controller, school):
        if back_button(school) is "S":
            controller.show_frame(StudentArea)
        elif back_button(school) is "T":
            controller.show_frame(TeacherArea)
        else:
            controller.show_frame(Main_Menu)


class ViewAccountInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        label = tk.Label(self, text="View Account Info", font=title_font)
        label.config(bg="blue", fg="white")
        label.pack(pady=10, padx=10, side="top", anchor="nw")

        self.w_header = None

        self.w_result = None

        self.header = tk.Label(self, text=self.w_header, font=large_font, bg="grey")
        self.header.pack()

        self.result = tk.Label(self, text=self.w_result, font=large_font, bg="grey")
        self.result.pack()

        photo = tk.PhotoImage(file="button.png")

        # Creates the button with the image stored
        help_button = tk.Button(self, text="Help Button", image=photo,
                                command=lambda: controller.show_frame(Help_Page))
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
                                command=lambda: self.changing_frame(
                                    controller, self.controller.shared_data["School"]))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)

    def changing_frame(self, controller, school):
        if back_button(school) is "S":
            controller.show_frame(StudentArea)
        elif back_button(school) is "T":
            controller.show_frame(TeacherArea)

    def on_show_frame(self, event):

        self.controller.update_widgets(
            [ViewAccountInfo], "header", "text", None)
        self.controller.update_widgets(
            [ViewAccountInfo], "result", "text", None)


class SetTestDate(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        self.controller = controller

        # Title Page of the second part of the Registration Form
        label = tk.Label(self, text="Set Test Date", font=title_font, bg="grey")
        label.grid(row=0, column=0)
        # Adds a separator between the form and instruction text
        separator = ttk.Separator(self, orient="vertical")
        separator.grid(row=1, column=3, rowspan=7, sticky="ns")
        # instruction text for username and password
        guide = ("""Enter test date, test type, test level and any other comments that you would like to add.
\n Note: Date format should be YYYY-MM-DD, leaving a comment is optional""")
        label_text = tk.Label(self, text=guide, font=small_font, bg="grey")
        label_text.grid(row=2, column=4)

        # Label for where the user enters their username
        test_label = tk.Label(self, text="Test Date", font=small_font, bg="grey")
        test_label.grid(row=1, column=0, pady=20)
        # Entry for username and the variable it is stored in
        test_entry = tk.Entry(self, textvariable=self.controller.shared_data["date"])
        test_entry.grid(row=1, column=1)

        # Label for where the user enters the test type
        type_label = tk.Label(self, text="Test Type", bg="grey", font=small_font)
        type_label.grid(row=2, column=0, pady=20)

        # Using tkinter radiobuttons to make check box for gender
        tk.Radiobutton(self, text="Pure", padx=5, variable=self.controller.shared_data["var_type"], value=1, bg="grey").grid(
            row=2, column=1)  # The options for the user gender value 1 (male) and the variable it is stored in
        tk.Radiobutton(self, text="Applied", padx=20, variable=self.controller.shared_data["var_type"], value=2, bg="grey").grid(
            row=2, column=2)  # the options for the user gender value 2 (female) and the variable it is stored in

        # Label for where the user enters whether the test is AS or A2
        level_label = tk.Label(self, text="Test Level", width=20,
                               font=small_font, bg="grey")
        level_label.grid(row=3, column=0, pady=20)

        # Using tkinter radiobuttons to make a check box for AS or A2
        tk.Radiobutton(self, text="AS", padx=5, variable=self.controller.shared_data["var_level"], value=1, bg="grey").grid(
            row=3, column=1)  # Option for the user either value 1 (AS) and the variable it is stored in
        tk.Radiobutton(self, text="A2", padx=20, variable=self.controller.shared_data["var_level"], value=2, bg="grey").grid(
            row=3, column=2)  # Option for the user either value 2 (A2) and the variable it is stored in

        comments_label = tk.Label(self, text="Comments", bg="grey", font=small_font)
        comments_label.grid(row=4, column=0)

        comments_entry = tk.Entry(
            self, textvariable=self.controller.shared_data["comments"])
        comments_entry.grid(row=4, column=1)

        # Terminates the whole program
        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(fg="white", bg="blue", height=3, width=10)
        quit_button.place(x=1200, y=750)
        # Alllows the user to go back to previous screen
        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(TeacherArea))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)

        create_button = tk.Button(self, text="Set Test Date", command=lambda: [self.test_date(controller, self.controller.shared_data["date"].get(), self.controller.shared_data["var_type"].get(),self.controller.shared_data["var_level"].get(), self.controller.shared_data["comments"].get()),test_entry.delete(0, tk.END),comments_entry.delete(0, tk.END)])
        create_button.config(bg="blue", fg="white", height=3, width=10)

        create_button.grid(row=5, column=2)

    def test_date(self, controller, date, type, level, comments):
        if set_test(date, type, level, comments) is True:
            messagebox.showinfo("Test", "Test Date has been set")
            controller.show_frame(TeacherArea)


class entry_questions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        self.controller = controller

        label = tk.Label(self, text="Questions", font=title_font, bg="grey")
        label.grid(row=0, column=0)

        intro_text ="""Please choose the question loop to occur either a pure question
        loop or applied question loop note the questions will have set answers \n and any rounding will be stated in the question"""

        guide = tk.Label(self, text=intro_text, bg="grey")
        guide.grid(row=2, column=4)

        separator = ttk.Separator(self, orient="vertical")
        separator.grid(row=1, column=3, rowspan=7, sticky="ns")

        type_label = tk.Label(self, text="Test Type", bg="grey")
        type_label.grid(row=2, column=0)

        tk.Radiobutton(self, text="Pure", padx=5,
                       variable=self.controller.shared_data["test_type"], value=1, bg="grey").grid(row=2, column=1)
        tk.Radiobutton(self, text="Applied", padx=5,
                       variable=self.controller.shared_data["test_type"], value=2, bg="grey").grid(row=2, column=2)
        start_button = tk.Button(self, text="Start", bg="grey", command=lambda: self.start_loop(
            self.controller, self.controller.shared_data["test_type"].get(), self.controller.shared_data["test_level"]))
        start_button.config(bg="blue", fg="white", height=3, width=10)
        start_button.grid(row=3, column=2)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(StudentArea))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(height=3, width=10, bg="blue", fg="white")
        quit_button.place(x=1200, y=750)

    def start_loop(self, controller, type, level):
        if type is 1 or type is 2:
            if type is 1:
                value = "Pure"
                self.controller.shared_data["Loop"] = "Pure"
            elif type is 2:
                value = "Applied"
                self.controller.shared_data["Loop"] = "Applied"
            self.controller.shared_data["Loop_type"] = value
            question_answer = get_question(value, level)
            self.controller.update_widgets([Question_Loop], "question", "text", question_answer[0])
            self.controller.shared_data["answer"] = question_answer[1]
            self.controller.show_frame(Question_Loop)
        else:
            messagebox.showerror("Questions", "Please choose either Pure or Applied")



class StudentandClass(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        self.controller = controller

        label = tk.Label(self, text="Student and Class Info", font=title_font, bg="grey")
        label.grid(row=0, column=0)

        order_age = tk.Button(self, text="Order by Age",
                              command=lambda: self.students.config(values=sc.sort_age()))
        order_age.config(height=3, width=15, bg="blue", fg="white")
        order_age.place(x=100, y=200)

        order_class = tk.Button(self, text="Order by Class",
                                command=lambda: self.students.config(values=sc.sort_class()))
        order_class.config(height=3, width=15, bg="blue", fg="white")
        order_class.place(x=300, y=200)

        order_surname = tk.Button(self, text="Order by Surname",
                                  command=lambda: self.students.config(values=sc.sort_surname()))
        order_surname.config(height=3, width=15, bg="blue", fg="white")
        order_surname.place(x=500, y=200)

        order_gender = tk.Button(self, text="Order by Gender",
                                 command=lambda: self.students.config(values=sc.sort_gender()))
        order_gender.config(height=3, width=15, bg="blue", fg="white")
        order_gender.place(x=700, y=200)

        order_forename = tk.Button(self, text="Order by Forename", command = lambda: self.students.config(values=sc.sort_forename()))
        order_forename.config(height=3,width=15,bg="blue",fg="white")
        order_forename.place(x=900,y=200)

        self.student = tk.StringVar()
        self.students = ttk.Combobox(self, values=sc.get_students(),
                                     state="readonly", textvariable=self.student)
        self.students.set("Please select a student")
        self.students.config(height=5, width=50)
        self.students.place(x=400, y=300)
        self.students.bind("<<ComboboxSelected>>", self.student_find)

        back_button = tk.Button(self, text="Back",
                                command=lambda: [controller.show_frame(TeacherArea),
                                                 self.students.set("Please select student")])
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(height=3, width=10, bg="blue", fg="white")
        quit_button.place(x=1200, y=750)

    def student_find(self, event):
        print(self.student.get()[0][0])
        self.controller.shared_data["student_id"] = self.student.get()[0][0]

        self.controller.update_widgets([MathsInfo], "score_result", "text", total_score(
            self.controller.shared_data["student_id"]))
        self.controller.show_frame(MathsInfo)


class Add_Question(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        self.controller = controller

        title_label = tk.Label(self, bg="grey", font=title_font, text="Add Question")
        title_label.grid(row=0, column=0)

        question_label = tk.Label(self, bg="grey", font=small_font, text="Question")
        question_label.grid(row=1, column=0)

        question_entry = tkst.ScrolledText(self, height=5, width=30, wrap=tk.WORD)
        question_entry.grid(row=1, column=1)

        type_label = tk.Label(self, bg="grey", text="Test Type", font=small_font)
        type_label.grid(row=2, column=0)

        tk.Radiobutton(self, text="Pure", padx=5, bg="grey", value=1,
                       variable=self.controller.shared_data["type"]).grid(row=2, column=1)
        tk.Radiobutton(self, text="Applied", padx=5, bg="grey", value=2,
                       variable=self.controller.shared_data["type"]).grid(row=2, column=2)
        level_label = tk.Label(self, bg="grey", text="Test Level", font=small_font)
        level_label.grid(row=3, column=0)

        tk.Radiobutton(self, text="AS", padx=5, bg="grey", value=1,
                       variable=self.controller.shared_data["level"]).grid(row=3, column=1)
        tk.Radiobutton(self, text="A2", bg="grey", value=2,
                       variable=self.controller.shared_data["level"]).grid(row=3, column=2)

        answer_label = tk.Label(self, text="Answer", bg="grey", font=small_font)
        answer_label.grid(row=4, column=0)

        answer = tk.StringVar()
        answer_entry = tk.Entry(self, textvariable=answer)
        answer_entry.grid(row=4, column=1)

        separator = ttk.Separator(self, orient="vertical")
        separator.grid(row=1, column=3, rowspan=7, sticky="ns")

        guide = """This allows you to create new questions for students the questions must have set answers \n and if the questions have more than one answer then separate using commas\n and if there is more than one answerthen separate the answers using commas """

        intro_label = tk.Label(self, text=guide, bg="grey", font=("Times New Roman", 10))
        intro_label.grid(row=2, column=4)

        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame(TeacherArea))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(height=3, width=10, bg="blue", fg="white")
        quit_button.place(x=1200, y=750)

        add_question = tk.Button(self, text="Add Question", command=lambda:
                                 [self.add_question(controller,
                                    question_entry.get("1.0", "end-1c"),
                                    self.controller.shared_data["type"].get(),
                                    self.controller.shared_data["level"].get(),
                                    answer.get()),
                                    question_entry.delete("1.0", "end")])
        add_question.config(bg="blue", fg="white", height=3, width=10)
        add_question.grid(row=5, column=2)

    def add_question(self, controller, question_text, type, level, answer):
        if make_question(question_text, type, level, answer) is True:
            messagebox.showinfo("Question", "Question has been added into the database")
            controller.show_frame(TeacherArea)


class Question_Loop(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        self.controller = controller
        title_label = tk.Label(self, text="Question Loop", bg="grey", font=title_font)
        title_label.grid(row=0, column=0)

        self.total = 0

        self.quizScore = 0
        self.correct = 0
        self.incorrect = 0

        self.question = tk.Label(self, text=" ", bg="grey", font=small_font)
        self.question.place(x=0, y=200)
        self.answer = tk.Label(self, text="Enter answer here", bg="grey", font=small_font)
        self.answer.place(x=500, y=450)
        userinput = tk.StringVar()

        self.entry = tk.Entry(self, textvariable=userinput)
        self.entry.place(x=700, y=450)

        self.check_answer = tk.Button(self, text="Confirm Anwser", command=lambda: [self.confirm_answer(
            self.controller, str(self.entry.get()), self.controller.shared_data["answer"]), self.entry.delete(0, tk.END)])
        self.check_answer.config(bg="blue", fg="white", height=3, width=15)
        self.check_answer.place(x=900, y=450)

        end_button = tk.Button(self, text="End Loop",
                               command=lambda: self.store_results(controller, self.controller.shared_data["Loop"], self.controller.shared_data["login_username"], self.correct, self.incorrect, self.quizScore, self.controller.shared_data["test_level"], self.total))
        end_button.config(height=3, width=10, bg="blue", fg="white")
        end_button.place(x=1050, y=750)

    def store_results(self, controller, loop,  user,  correct, incorrect, score, level, total):
        if end_loop(loop, user, correct, incorrect, score, level, total) is True:
            messagebox.showinfo("Results", "End of Questions Result are correct: %s, incorrect: %s, score: %s, total: %s" % (
                self.correct, self.incorrect, self.quizScore, self.total))
            self.total = 0
            self.correct = 0
            self.quizScore=0
            self.incorrect =0
            
            controller.show_frame(StudentArea)
        elif end_loop(loop, user, correct, incorrect, score, level, total) is False:
            messagebox.showinfo("Questions", "No Questions attempted")
            controller.show_frame(StudentArea)

    def confirm_answer(self,controller, user_answer, actual_answer):
        if compare_answers(user_answer, actual_answer) is True:
            messagebox.showinfo("Answer", "That is the correct answer")
            self.total = self.total + 1
            self.correct = self.correct + 1
            self.quizScore = self.quizScore + 5
            question_answer = get_question(self.controller.shared_data["Loop_type"],
                                       self.controller.shared_data["test_level"])
            self.question["text"] = question_answer[0]
            if question_answer[1] == "END":
                end_loop(self.controller.shared_data["Loop"],
                         self.controller.shared_data["login_username"],
                         self.correct,self.incorrect,self.quizScore,
                         self.controller.shared_data["test_level"],self.total)
                messagebox.showinfo("Results", """End of questions (no more questions)
                Results are correct:%s, incorrect:%s, score:%s, total:%s""" % (
                                   self.correct, self.incorrect, self.quizScore, self.total))
                self.correct=0
                self.incorrect=0
                self.total=0
                self.quizScore = 0
                self.controller.show_frame(StudentArea)
            else:
                self.controller.shared_data["answer"] = question_answer[1]
        elif compare_answers(user_answer, actual_answer) is False:
            messagebox.showinfo("Answer", "That is incorrect answer is %s" %
                                (self.controller.shared_data["answer"]))
            self.total = self.total + 1
            self.incorrect = self.incorrect + 1
            self.quizScore = self.quizScore - 5
            question_answer = get_question(self.controller.shared_data["Loop_type"],
                                           self.controller.shared_data["test_level"])
            self.question["text"] = question_answer[0]
            if question_answer[1] == "END":
                end_loop(self.controller.shared_data["Loop"],
                         self.controller.shared_data["login_username"],
                         self.correct,self.incorrect,self.quizScore,
                         self.controller.shared_data["test_level"],self.total)
                messagebox.showinfo("Results", """End of questions (no more questions)
                Results are correct:%s, incorrect:%s, score:%s, total:%s""" % (
                    self.correct, self.incorrect, self.quizScore, self.total))
                self.correct=0
                self.incorrect=0
                self.total=0
                self.quizScore = 0
                self.controller.show_frame(StudentArea)
            else:
                self.controller.shared_data["answer"] = question_answer[1]


class MathsInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="grey")
        self.controller = controller
        title_label = tk.Label(self, text="Maths Info", font=title_font, bg="grey")
        title_label.grid(row=0, column=0)

        correct_results = tk.Button(self, text="Correct Graphs",command= lambda: [end(), correct_graphs(
            self.controller.shared_data["student_id"])])
        correct_results.config(height=5, width=20, bg="blue",fg="white")
        correct_results.place(x=525, y=200)

        total_correct_results = tk.Button(self, text="Total Correct Graph", command=lambda: [end(),total_graph_correct(
            self.controller.shared_data["student_id"])])
        total_correct_results.config(height=5, width=20, bg="blue", fg="white")
        total_correct_results.place(x=200, y=200)

        incorrect_results = tk.Button(self, text="Incorrect Graphs",command= lambda: [end(), incorrect_graphs(
            self.controller.shared_data["student_id"])])
        incorrect_results.config(height=5, width=20, bg="blue",fg="white")
        incorrect_results.place(x=525, y=400)

        total_incorrect_results = tk.Button(self, text="Total Incorrect Graph", command=lambda: [end(),total_graph_incorrect(
            self.controller.shared_data["student_id"])])
        total_incorrect_results.config(height=5, width=20, bg="blue", fg="white")
        total_incorrect_results.place(x=850, y=200)

        total_results = tk.Button(self, text="Total Questions Graph", command=lambda: [end(),graph_total_questions(
            self.controller.shared_data["student_id"])])
        total_results.config(height=5, width=20, bg="blue", fg="white")
        total_results.place(x=850, y=400)

        total_score = tk.Button(self, text="Total Score Graph", command=lambda: [end(),
        score_graph(self.controller.shared_data["student_id"])])
        total_score.config(height=5,width=20,bg="blue", fg="white")
        total_score.place(x=200, y=400)
        
        score_label = tk.Label(self, text="Score:", bg="grey", font=large_font)
        score_label.place(x=300, y=600)
        self.score_result = tk.Label(self, text="", bg="grey", font=large_font)
        self.score_result.place(x=400, y=600)

        back_button = tk.Button(self, text="Back",
                                command=lambda: self.changing_frame(controller, self.controller.shared_data["School"]))
        back_button.config(height=3, width=10, bg="blue", fg="white")
        back_button.place(x=1050, y=750)

        quit_button = tk.Button(self, text="Exit", command=lambda: quit(self))
        quit_button.config(height=3, width=10, bg="blue", fg="white")
        quit_button.place(x=1200, y=750)

    def changing_frame(self, controller, school):
        if back_button(school) is "S":
            controller.show_frame(StudentArea)
        elif back_button(school) is "T":
            controller.show_frame(TeacherArea)

if __name__ == "__main__":
    root = MathsPro()  # this runs the Maths Pro class
    root.geometry("1280x800+150-50")  # changes the size of the window
    root.resizable(width=False, height=False)  # Prevents the root size from being changed
    root.mainloop()  # As MathsPro inherited from tkinter this function can be moved
