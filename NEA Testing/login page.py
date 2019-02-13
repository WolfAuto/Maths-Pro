import tkinter as tk
from tkinter import ttk
from login_backend import login_in, forgot_password, support_email

from tkinter import messagebox
title_font = ("Times New Roman", 50)
medium_font = ("Times New Roman", 20)
small_font = ("Times New Roman", 12)  # Setting fonts for small deails to be displayed


class MathsPro(tk.Tk):  # Creating a class that inherits from tk.Tk

    def __init__(self, *args, **kwargs):  # intialises the object
        # intialises the object as a tkinter frame
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="")
        # Sets the title of each page to be Maths Pro
        tk.Tk.wm_title(self, "Maths Pro")
        # defined a container for all the frames to be kept
        container = tk.Frame(self)

        # The containter is filled with a bunch of frames
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        # After the page being packed this allows it to be displayed correctly
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # Empty dictionary where all the frames are kept

        # contains all the pages being used #this will not work without pages
        for F in (Main_Menu, StudentArea, TeacherArea, Help_Page):

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
        title_label = tk.Label(self, text="Maths Pro", bg="blue", fg="white", font=title_font)
        title_label.pack(pady=10, padx=10, fill="x")
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

        register_button = tk.Button(self, text="Register")
        register_button.config(height=3, width=15, bg="blue", fg="white")
        register_button.place(x=720, y=420)

        button1 = ttk.Button(self, text="Student Area",
                             command=lambda: controller.show_frame(StudentArea))
        button1.pack(side="right", anchor="e")

        button2 = ttk.Button(self, text="Teacher Area",
                             command=lambda: controller.show_frame(TeacherArea))
        button2.pack(side="right", anchor="w")

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
        elif login_in(username, password) == "T":
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
        account_button.config(height=5, width=30, bg="blue", fg="white")
        account_button.place(x=400, y=450)

        info_button = tk.Button(self, text="View Maths Information")
        info_button.config(height=5, width=30, bg="blue", fg="white")
        info_button.place(x=750, y=450)

        math_button1 = tk.Button(self, text="AS Maths")
        math_button1.config(height=5, width=30, bg="blue", fg="white")
        math_button1.place(x=400, y=250)

        math_button2 = tk.Button(self, text="A2 Maths")
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

        account_info = tk.Button(self, text="View Account Information")
        account_info.config(height=5, width=30, bg="blue", fg="white")
        account_info.place(x=750, y=450)

        student_class_information = tk.Button(self, text="View Student/Class Information")
        student_class_information.place(x=400, y=250)
        student_class_information.config(height=5, width=30, bg="blue", fg="white")

        flagged_students = tk.Button(self, text="View Flagged Students")
        flagged_students.place(x=750, y=250)
        flagged_students.config(height=5, width=30, bg="blue", fg="white")

        test_date = tk.Button(self, text="Set Test Date")
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


class Help_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="cyan")

        label = tk.Label(self, text="Help Page", font=title_font)
        label.config(bg="cyan")
        label.pack(pady=10, padx=10, side="top", anchor="nw")

        def toggle():
            if label_1.invisible:
                label_1.place_forget()
            else:
                label_1.place(x=300, y=110)
            label_1.invisible = not(label_1.invisible)

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
            self, text="Maths Pro is a revision app around maths \n that allows for continuous revision on A level Maths", bg="cyan", font=small_font)
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
            "If you still have problems or which to recommend any updates you can email Maths Pro \n using the button below")
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
                                command=lambda: controller.show_frame(Main_Menu))
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


root = MathsPro()  # this runs the Maths Pro class
root.geometry("1280x800+150-50")  # changes the size of the window
root.resizable(width=False, height=False)
root.mainloop()  # As MathsPro inherited from tkinter this function can be moved
