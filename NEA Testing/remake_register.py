import sqlite3 as sql  # module for database connection
from tkinter import messagebox  # module for error messages on the tkinter page
import string
with sql.connect("newfile.db") as db:  # sets the connection to tbe database file
    global cursor  # makes the cursor a global variable for all parts of the program
    cursor = db.cursor()  # sets the cursor to allow sql statement execution

create_student_table = ("""CREATE TABLE IF NOT EXISTS Students(account_id INTEGER PRIMARY KEY,
                        firstname VARCHAR(30),
                        surname VARCHAR(30) ,  age INTEGER ,
                        class VARCHAR (3), gender VARCHAR (30) ,
                         username VARCHAR(30),password VARCHAR(30), email VARCHAR(30))""")

create_teacher_table = ("""CREATE TABLE IF NOT EXISTS Teachers(account_id INTEGER PRIMARY KEY,
                        firstname VARCHAR(30) ,
                        surname VARCHAR(30) ,  age INTEGER ,
                        class VARCHAR (3) , gender VARCHAR (30),
                         username VARCHAR(30), password VARCHAR(30), email VARCHAR(30))""")
# Sql statment to create the table where the user information will be stored
cursor.execute(create_student_table)  # executes the sql statement

# Sql statment to create the table where the user information will be stored
cursor.execute(create_teacher_table)  # executes the sql statement
db.commit()  # saves changes made to the sql file


def register1(firstname, surname, age, school_class, var, var1):# Function for registration
    gender=""
    if firstname.isalpha() == True:
        if surname.isalpha() == True:
            try:
                age1=int(age)
                if school_class.isalnum() == True:
                    if var == 1:  # changing the var to a gender either male or female depending on value
                        if (var1==1) or (var1==2):
                            print(firstname, surname, age, school_class, var1)
                            return "m"
                        else:
                            messagebox.showwarning(
                                "School", "Please choose either Student or Teacher")
                            return False
                        
                    elif var == 2:
                        if (var1==1) or (var1==2):
                            print(firstname, surname, age, school_class, var1)
                            return "f"
                        else:
                            messagebox.showwarning(
                                "School", "Please choose either Student or Teacher")
                            return False
                    else:
                        messagebox.showwarning("Gender", "Gender option cannot be left blank")
                        return False
                else:
                    messagebox.showwarning("Class", "Class option cannot be left blank")
            except ValueError:
                messagebox.showwarning("Age", "Please enter a number")
        else:
            messagebox.showwarning("Surname", "Please enter a Proper Surname")
    else:
        messagebox.showwarning("First Name", "Please enter a proper First Name")



def username_check(username):  # function for username vaildation
    # Checking the length of username is more than 6 charcters
    if len(username) >= 6:
        # sql statement for checking existing users
        existing_users = cursor.execute(
            "SELECT Students.username, Teachers.username from Students INNER JOIN Teachers USING(account_id)")
        checking = cursor.fetchall()  # stores the result of sql search
        if checking:  # if a username matches the username typed it returns false
            # tkinter error message
            messagebox.showwarning(
                "Username", "That username has already been taken please try another username")
            return False
        else:
            return True
    else:
        messagebox.showwarning(
            "Username", "Username has to be 6 or more characters")
        return False


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
                            if password == password_confirm:  # ensures that the two password variables match
                                return True
                            else:
                                messagebox.showwarning(
                                    "Password", "Passwords don't match re enter confirm password again")
                                # tkinter error message
                                return False
                        else:
                            messagebox.showwarning(
                                "Password", "Password doesn't contain a special character")
                            return False
                    else:
                        # tkinter error message
                        messagebox.showwarning(
                            "Password", "Password don't contain digits character")
                        return False
                else:
                    messagebox.showwarning(
                        "Password", "Password don't contain any uppercase characters")  # tkinter error message
                    return False
            else:
                messagebox.showwarning(
                    "Password", "Password don't contain any lowercase letters")  # tkinter error message
            return False
        else:
            messagebox.showwarning(
                "Password", "Password is not 8 characters long")  # tkinter error message
            return False
    else:
        messagebox.showwarning(
            "Password", "Password don't match")  # tkinter error message
        return False


def email_check(email):  # function for email vaildation
    if email.find("@") == -1:  # checks for a @ sign
        messagebox.showwarning("Email", "Email must contain a @ sign")
        return False
    # checks for a . and ensures that it is after the @
    elif email.find(".") < (email.find("@") + 2):
        messagebox.showwarning(
            "Email", "Email must contain a . after the @ sign")
        return False
    elif email.find(" ") != -1:  # ensures there are no spaces
        messagebox.showwarning("Email", "Email must not contain any spaces")
        return False
    else:
        return True


# function for entering a record into accounts
def register2(username, password, confirm_password, email, var1):
    # checks whether a existing username with the username enter exists
    if username_check(username):
        # ensures the password passes all the vaildations
        if password_check(password, confirm_password):
            if email_check(email):  # ensures the email passes the vaildation
                if var1 == 1: # inserts one whole record into student table
                    insert_student = ("INSERT INTO Students(firstname,surname,age,class,gender,username,password,email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
                    cursor.execute(insert_student, [(self.controller.shared_data["firstname"].get()), (self.controller.shared_data["surname"].get()),
                                                    (self.controller.shared_data["age"].get()), (self.controller.shared_data["Class"].get()),
                                                    (self.controller.shared_data["gender"].get()), (username), (password), (email)])
                elif var1 == 2: # inserts one whole record into the teacher table
                    insert_teacher = ("INSERT INTO Teachers(firstname,surname,age,class,gender,username,password,email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
                    cursor.execute(insert_teacher, [(self.controller.shared_data["firstname"].get()), (self.controller.shared_data["surname"].get()),
                                                    (self.controller.shared_data["age"].get()), (self.controller.shared_data["Class"].get()),
                                                    (self.controller.shared_data["gender"].get()), (username), (password), (email)])

                db.commit()  # saves the changes to the database file
                db.close()  # closes the connection to the database file
                return True
            else:
                messagebox.showwarning("Warning Email Address",
                                       "Please enter a vaild email address")  # tkinter error message
                return False
        else:
            return False
    else:
        messagebox.showwarning(
            "Warning Username", "That username is already taken please try another one")  # tkinter error message
        return False
