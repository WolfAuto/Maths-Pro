import sqlite3 as sql  # module for database connection
from tkinter import messagebox  # module for error messages on the tkinter page
import string
import re
import bcrypt
from validate_email import validate_email
import yagmail
with sql.connect("updatedfile.db") as db:  # sets the connection to tbe database file
    global cursor  # makes the cursor a global variable for all parts of the program
    global cursor1
    cursor = db.cursor()  # sets the cursor to allow sql statement execution
    cursor1 = db.cursor()
shared_data = {"firstname": "blank",  # dictionary that stores the user register information
               "surname": "blank",    # through using the controller we can pass these variables
               "age": 0,        # to different frames
               "Class": "blank",
               "gender": "blank", }
create_student_table = ("""CREATE TABLE IF NOT EXISTS Students(account_id INTEGER PRIMARY KEY,
                        firstname VARCHAR(30),
                        surname VARCHAR(30) ,  age INTEGER ,
                        class VARCHAR (3), gender VARCHAR (30) ,
                         username VARCHAR(30),password VARCHAR(80), email VARCHAR(30))""")

create_teacher_table = ("""CREATE TABLE IF NOT EXISTS Teachers(account_id INTEGER PRIMARY KEY,
                        firstname VARCHAR(30) ,
                        surname VARCHAR(30) ,  age INTEGER ,
                        class VARCHAR (3) , gender VARCHAR (30),
                         username VARCHAR(30), password VARCHAR(80), email VARCHAR(30))""")
# Sql statment to create the table where the user information will be stored
cursor.execute(create_student_table)  # executes the sql statement

# Sql statment to create the table where the user information will be stored
cursor.execute(create_teacher_table)  # executes the sql statement
db.commit()  # saves changes made to the sql file


def register1(firstname, surname, age, school_class, var, var1):  # Function for registration
    if firstname.isalpha() is True:
        if surname.isalpha() is True:
            try:
                age1 = int(age)
                if school_class.isalnum() is True:
                    if var == 1:  # changing the var to a gender either male or female depending on value
                        if (var1 == 1) or (var1 == 2):
                            shared_data["firstname"] = firstname
                            shared_data["surname"] = surname
                            shared_data["age"] = age1
                            shared_data["gender"] = "Male"
                            shared_data["Class"] = school_class
                            return True
                        else:
                            messagebox.showerror(
                                "School", "Please choose either Student or Teacher")
                            return False

                    elif var == 2:
                        if (var1 == 1) or (var1 == 2):
                            shared_data["firstname"] = firstname
                            shared_data["surname"] = surname
                            shared_data["age"] = age1
                            shared_data["gender"] = "Female"
                            shared_data["Class"] = school_class
                            return True
                        else:
                            messagebox.showerror(
                                "School", "Please choose either Student or Teacher")
                            return False
                    else:
                        messagebox.showerror("Gender", "Gender option cannot be left blank")
                        return False
                else:
                    messagebox.showerror("Class", "Class option cannot be left blank")
            except ValueError:
                messagebox.showerror("Age", "Please enter a number")
        else:
            messagebox.showerror("Surname", "Please enter a Proper Surname")
    else:
        messagebox.showerror("First Name", "Please enter a proper First Name")


def username_check(username):  # function for username vaildation
    # Checking the length of username is more than 6 charcters
    if len(username) >= 6:
        # sql statement for checking existing users
        # Checks student database for username
        fetchstudents = ("SELECT DISTINCT Students.username from Students WHERE username = ?")
        # Checkes teacher databaase for username
        fetchteachers = ("SELECT DISTINCT Teachers.username from Teachers WHERE username = ?")
        cursor.execute(fetchstudents, [(username)])  # executes the above query on the student table
        cursor1.execute(fetchteachers, [(username)])  # execute the above query on the teacher table
        checking = cursor.fetchall()  # stores the result of sql search
        checking1 = cursor1.fetchall()
        if checking or checking1:
            messagebox.showerror("Username", "That username has been taken please try another one")
        else:
            return True

    else:
        messagebox.showerror(
            "Username", "Username has to be 6 or more characters")


def password_check(password, password_confirm):  # function for password vaildation
    if password == password_confirm:
        if len(password) >= 8:  # checks whether the password length is 8 chracterslong
            # checks for letters in the password
            if len(set(string.ascii_lowercase).intersection(password)) > 0:
                # checks for numbers or special characters in the password
                if (len(set(string.ascii_uppercase).intersection(password)) > 0):
                    # checks for uppercase characters
                    if (len(set(string.digits).intersection(password))) > 0:
                        if (len(set(string.punctuation).intersection(password))) > 0:
                            return True
                        else:
                            messagebox.showerror(
                                "Password", "Password doesn't contain a special character")
                            return False
                    else:
                        # tkinter error message
                        messagebox.showerror(
                            "Password", "Password don't contain numbers")
                        return False
                else:
                    messagebox.showerror(
                        "Password", "Password don't contain any uppercase characters")  # tkinter error message
                    return False
            else:
                messagebox.showerror(
                    "Password", "Password don't contain any lowercase letters")  # tkinter error message
            return False
        else:
            messagebox.showerror(
                "Password", "Password is not 8 characters long")  # tkinter error message
            return False
    else:
        messagebox.showerror(
            "Password", "Password don't match")  # tkinter error message
        return False


def email_check(email):  # function for email vaildation
    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    is_valid = validate_email(email, verify=True)

    if match is None:
        messagebox.showerror("Email", "Please enter a valid email address ")
    if is_valid is not True:
        messagebox.showerror(
            "Email", "Email address doesn't exist please try another email address")
    else:
        return True


def register2(username, password, confirm_password, email, var1):
    # checks whether a existing username with the username enter exists
    if username_check(username):
        # ensures the password passes all the vaildations
        if password_check(password, confirm_password):
            password_store = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())
            if email_check(email):  # ensures the email passes the vaildation
                if var1 == 1:  # inserts one whole record into student table
                    insert_student = (
                        "INSERT INTO Students(firstname,surname,age,class,gender,username,password,email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
                    cursor.execute(insert_student, [(shared_data["firstname"]), (shared_data["surname"]),
                                                    (shared_data["age"]), (shared_data["Class"]),
                                                    (shared_data["gender"]), (username), (password_store), (email)])
                    send_email(email, username)

                elif var1 == 2:  # inserts one whole record into the teacher table
                    insert_teacher = (
                        "INSERT INTO Teachers(firstname,surname,age,class,gender,username,password,email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
                    cursor.execute(insert_teacher, [(shared_data["firstname"]), (shared_data["surname"]),
                                                    (shared_data["age"]), (shared_data["Class"]),
                                                    (shared_data["gender"]), (username), (password_store), (email)])
                    send_email(email, username)

                db.commit()  # saves the changes to the database file
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def send_email(email, username):
    yag = yagmail.SMTP("mathspro0@gmail.com", oauth2_file="~/oauth2_creds1.json")
    send_mail = (" Email Confirmation From Maths Pro",
                 " First Name:" + shared_data["firstname"],
                 "Surname:" + shared_data["surname"],
                 " Age:" + str(shared_data["age"]),
                 "Class: " + shared_data["Class"],
                 "Gender:" + shared_data["gender"],
                 "username:" + username)
    yag.send(to=email, subject="Maths Pro Email Confirmation", contents=send_mail)
