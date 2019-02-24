import sqlite3 as sql
import bcrypt
import yagmail
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from remake_register import password_check
with sql.connect("updatedfile.db") as db:
    cursor = db.cursor()
    cursor1 = db.cursor()


def back_button(school):
    if school is "Student":
        return "S"
    elif school is "Teacher":
        return "T"
    else:
        return "M"


def login_in(username, password):
    if student_check(username, password) is True and teacher_check(username, password) is False:
        return "S"
    elif student_check(username, password) is False and teacher_check(username, password) is True:
        return "T"
    else:
        return False


def forgot_password(email, new_pass, confirm_pass):
    if password_check(new_pass, confirm_pass) is True:
        password_store = bcrypt.hashpw(new_pass.encode("utf8"), bcrypt.gensalt())
        if (student_email(email) is not False and teacher_email(email) is False):
            update_student = ("UPDATE Students SET password=? WHERE email=?")
            cursor.execute(update_student, [(password_store), (email)])
            db.commit()
            return True

        elif (student_email(email) is False and teacher_email(email) is not False):
            update_teacher = ("UPDATE Teachers SET password=? WHERE email=?")
            cursor.execute(update_teacher, [(password_store), (email)])
            db.commit()
            return True
        else:
            messagebox.showerror(
                "Email", "Email doesn't exist either message support or register as you haven't made an account")
    else:
        pass


def student_check(username, password):
    find_user = ("SELECT username,password FROM Students WHERE username = ?")
    cursor.execute(find_user, [(username)])
    checking = cursor.fetchone()
    if checking is not None:
        db_user, db_password = checking
        if (username == db_user) and (bcrypt.checkpw(password.encode("utf8"), db_password) is True):
            return True
    else:
        return False


def teacher_check(username, password):
    find_user1 = ("SELECT username,password FROM Teachers WHERE username = ?")
    cursor1.execute(find_user1, [(username)])
    checking1 = cursor1.fetchone()
    if checking1 is not None:
        db_user1, db_password1 = checking1
        if (username == db_user1) and (bcrypt.checkpw(password.encode("utf8"), db_password1) is True):
            return True
    else:
        return False


def student_email(email):
    find_student = ("SELECT Students.email FROM Students WHERE email = ?")
    cursor.execute(find_student, [(email)])
    result = cursor.fetchone()
    if result is not None:
        db_email = result
        if email == db_email:
            return True

    else:
        return False


def teacher_email(email):
    find_teacher = ("SELECT Teachers.email FROM Teachers WHERE email = ?")
    cursor1.execute(find_teacher, [(email)])
    checking = cursor1.fetchone()
    if checking is not None:
        db_email = checking
        if email == db_email:
            return True
    else:
        return False


def support_email():
    support_window = tk.Tk()
    support_window.withdraw()

    yag = yagmail.SMTP("mathspro0@gmail.com", oauth2_file="~/oauth2_creds1.json")

    text = simpledialog.askstring(
        "Input", "Enter your problem or advice to send to Maths Pro", parent=support_window)

    send_mail = ("Email to Maths Pro",
                 text)
    if text is not None:
        yag.send(subject="Maths Pro Support Email", contents=send_mail)
        support_window.destroy()
        return True
    else:
        return messagebox.showerror(
            "Support", "Please don't leave support message blank and \n send reasonable messages to support email Thank You")
        support_window.destroy()
