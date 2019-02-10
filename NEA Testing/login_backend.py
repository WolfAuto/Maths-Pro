import sqlite3 as sql
import bcrypt
from tkinter import messagebox
from remake_register import password_check
with sql.connect("updatedfile.db") as db:
    global cursor
    cursor = db.cursor()
    cursor1 = db.cursor()


def login_in(username, password):
    if student_check(username, password) is True and teacher_check(username, password) is False:
        return "S"
    elif student_check(username, password) is False and teacher_check(username, password) is True:
        return "T"
    else:
        return False


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
    find_student = ("SELECT email FROM Students WHERE email = ?")
    cursor.execute(find_student, [(email)])
    checking = cursor.fetchone()
    if checking is not None:
        db_email = checking
        if email == db_email:
            return True
    else:
        return False


def teacher_email(email):
    find_teacher = ("SELECT email FROM Teachers WHERE email = ?")
    cursor.execute(find_teacher, [(email)])
    checking = cursor.fetchone()
    if checking is not None:
        db_email = checking
        if email == db_email:
            return True
    else:
        return False


def forgot_password(email, new_pass, confirm_pass):
    if password_check(new_pass, confirm_pass) is True:
        password_store = bcrypt.hashpw(new_pass.encode("utf8"), bcrypt.gensalt())
        if (student_email(email) is True) and (teacher_email(email) is False):
            update_student = ("UPDATE Students SET password=? WHERE email=?")
            cursor.execute(update_student, [(password_store), (email)])
            db.commit()
            db.close()
            messagebox.showinfo("Password", "Password has been changed")

        elif teacher_email(email) is True and student_email(email) is False:
            update_teacher = ("UPDATE Teachers SET password=? WHERE email=?")
            cursor.execute(update_teacher, [(password_store), (email)])
            db.commit()
            db.close()
            messagebox.showinfo("Password", "Password has been changed")
    else:
        pass
