import sqlite3 as sql  # module for database connection
from tkinter import messagebox  # module for error messages on the tkinter page
import string
with sql.connect("testing.db") as db:  # sets the connection to tbe database file
    global cursor  # makes the cursor a global variable for all parts of the program
    cursor = db.cursor()  # sets the cursor to allow sql statement execution

create_personal_details = ("""CREATE TABLE IF NOT EXISTS personal_details
                           (account_id INTEGER PRIMARY KEY NOT NULL, firstname VARCHAR(30) NOT NULL,
                           surname VARCHAR(30) NOT NULL,  age INTEGER NOT NULL,
                           class VARCHAR (3) NOT NULL, gender VARCHAR (30) NOT NULL,
                           school VARCHAR (30) NOT NULL,
                           FOREIGN KEY(account_id) REFERENCES accounts(account_id))""")

cr
# Sql statment to create the table where the user information will be stored
cursor.execute(create_personal_details)  # executes the sql statement
create_accounts = ("""CREATE TABLE IF NOT EXISTS accounts
                   (account_id INTEGER PRIMARY KEY NOT NULL, username VARCHAR(30),
                   password VARCHAR(30), email VARCHAR(30))""")
# Sql statment to create the table where the user information will be stored
cursor.execute(create_accounts)  # executes the sql statement
db.commit()  # saves changes made to the sql file


def register1(firstname, surname, age, school_class, var, var1):  # Function for registration
    Age = int(age)  # ensures the age is a number
    if var == 1:  # changing the var to a gender either male or female depending on value
        gender = "Male"
    elif var == 2:
        gender = "Female"
    if var1 == 1:  # changin the var1 to a school either student or teacher depending on value
        School = "Student"
    elif var1 == 2:
        School = "Teacher"
    print(firstname, surname, Age, school_class, gender, School)  # for testing purposes
    insert_details = (
        """INSERT INTO personal_details (firstname,surname, age, class, gender, school)
        VALUES (?, ? , ? , ? , ?, ?)""")  # sql statement to insert a record into table personal_details
    cursor.execute(insert_details, [(firstname), (surname),
                                    (Age), (school_class), (gender), (School)])  # execution of sql statement
    db.commit()  # saves changes made to the database file
    return True  # this is to ensure the record has been made to move to the next part of the registration


def username_check(username):  # function for username vaildation
    # sql statement for checking existing users
    existing_users = ("SELECT * from accounts WHERE username = ?")
    cursor.execute(existing_users, [(username)])  # execution of sql statement
    checking = cursor.fetchall()  # stores the result of sql search
    if checking:  # if a username matches the username typed it returns false
        messagebox.showerror(
            "Error", "That username has already been taken please try another username")  # tkinter error message
        return False
    else:
        return True


def password_check(password, password_confirm):  # function for password vaildation
    if password == password_confirm:
        if len(password) >= 8:  # checks whether the password length is 8 chracterslong
            if len(set(string.ascii_lowercase).intersection(password)) > 0:  # checks for letters in the password
                # checks for numbers or special characters in the password
                if (len(set(string.ascii_uppercase).intersection(password)) > 0):
                    if (len(set(string.ascii_digit).intersection(password))) > 0:  # checks for uppercase characters
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


def register2(username, password, confirm_password, email):  # function for entering a record into accounts
    if username_check(username):  # checks whether a existing username with the username enter exists
        if password_check(password, confirm_password):  # ensures the password passes all the vaildations
            if email_check(email):  # ensures the email passes the vaildation
                insert_account = (
                    "INSERT INTO accounts (username, password, email) VALUES (? , ? , ?)")
                # sql statement for inserting a record into accounts
                # executes the sql statement
                cursor.execute(insert_account, [(username), (password), (email)])
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
