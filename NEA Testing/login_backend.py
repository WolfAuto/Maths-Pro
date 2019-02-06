import sqlite3 as sql
import bcrypt
with sql.connect("newfile.db") as db:
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
        if (username == db_user1) and (bcrypt.checkpw(password.encode("utf8"), db_password) is True):
            return True
    else:
        return False
