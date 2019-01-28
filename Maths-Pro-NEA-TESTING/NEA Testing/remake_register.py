import sqlite3 as sql  # module for database connection
from tkinter import messagebox  # module for error messages on the tkinter page
import string
with sql.connect("newfile.db") as db:  # sets the connection to tbe database file
    global cursor  # makes the cursor a global variable for all parts of the program
    cursor = db.cursor()  # sets the cursor to allow sql statement execution

create_student_table = ("""CREATE TABLE IF NOT EXISTS students(account_id INTEGER PRIMARY KEY,
                        firstname VARCHAR(30) NOT NULL,
                        surname VARCHAR(30) NOT NULL,  age INTEGER NOT NULL,
                        class VARCHAR (3) NOT NULL, gender VARCHAR (30) NOT NULL,
                         username VARCHAR(30),password VARCHAR(30), email VARCHAR(30))""")

create_teacher_table = ("""CREATE TABLE IF NOT EXISTS teachers(account_id INTEGER PRIMARY KEY,
                        firstname VARCHAR(30) NOT NULL,
                        surname VARCHAR(30) NOT NULL,  age INTEGER NOT NULL,
                        class VARCHAR (3) NOT NULL, gender VARCHAR (30) NOT NULL,
                         username VARCHAR(30), password VARCHAR(30), email VARCHAR(30))""")
# Sql statment to create the table where the user information will be stored
cursor.execute(create_student_table)  # executes the sql statement

# Sql statment to create the table where the user information will be stored
cursor.execute(create_teacher_table)  # executes the sql statement
db.commit()  # saves changes made to the sql file


def register1(firstname, surname, age, school_class, var, var1):  # Function for registration
    # if firstname.isalpha() == True:
    #    if surname.isalpha() == True:
    #        if age != "" and age.isdigit() == True:
    Age = int(age)  # ensures the age is a number
    if var == 1:  # changing the var to a gender either male or female depending on value
        gender = "Male"
    elif var == 2:
        gender = "Female"
    if var1 == 1:  # changin the var1 to a school either student or teacher depending on value
        insert_details = (
            """INSERT INTO students(firstname, surname, age, class, gender)
            VALUES(?, ?, ?, ?, ?)""")  # sql statement to insert a record into table students
        cursor.execute(insert_details, [(firstname), (surname),
                                        (Age), (school_class), (gender)])  # execution of sql statement
    elif var1 == 2:
        insert_details = (
            """INSERT INTO teachers(firstname, surname, age, class, gender)
            VALUES(?, ?, ?, ?, ?)""")  # sql statement to insert a record into table teacher
        cursor.execute(insert_details, [(firstname), (surname),
                                        (Age), (school_class), (gender)])  # execution of sql statement
    print(firstname, surname, Age, school_class,
          gender)  # for testing purposes
    # db.commit()  # saves changes made to the database file
    return True  # this is to ensure the record has been made to move to the next part of the registration


def username_check(username):  # function for username vaildation
    # Checking the length of username is more than 6 charcters
    if len(username) >= 6:
        # sql statement for checking existing users
        existing_users = cursor.execute(
            "SELECT * from student,teacher where username = ?", (username,))

        checking = cursor.fetchall()  # stores the result of sql search
        if checking:  # if a username matches the username typed it returns false
            messagebox.showerror(
                "Username", "That username has already been taken please try another username")  # tkinter error message
            return False
        else:
            return True
    else:
        messagebox.showerror("Username", "Username has to be 6 or more characters")


def password_check(password, password_confirm):  # function for password vaildation
    if password == password_confirm:
        if len(password) >= 8:  # checks whether the password length is 8 chracterslong
            # checks for letters in the password
            if len(set(string.ascii_lowercase).intersection(password)) > 0:
                # checks for numbers or special characters in the password
                if (len(set(string.ascii_uppercase).intersection(password)) > 0):
                    # checks for uppercase characters
                    if (len(set(string.ascii_digit).intersection(password))) > 0:
                        if (len(set(string.ascii_punctuation).intersection(password))) > 0:
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
        return False
    elif email.find(".") < (email.find("@") + 2):  # checks for a . and ensures that
        return False
    elif email.find(" ") != -1:  # ensures there are no spaces
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
                if var1 == 1:
                    insert_student = (
                        "INSERT INTO students(username,password,email) VALUES (?, ?, ?)")
                    cursor.execute(insert_student, [
                                   (username), (password), (email,)])
                elif var1 == 2:
                    insert_teacher = (
                        "INSERT INTO teachers(username,password,email) VALUES (?, ?, ?)")
                    cursor.execute(insert_student, [
                                   (username), (password), (email)])

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
