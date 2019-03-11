
from tkinter import messagebox
import datetime as dt
from create_connection import *

current_date = dt.date.today().strftime("%Y-%m-%d")
create_result_table = """CREATE TABLE IF NOT EXISTS maths_result(maths_id INTEGER PRIMARY KEY , score INTEGER, correct_pure INTEGER, correct_applied INTEGER, incorrect_pure INTEGER, incorrect_applied INTEGER, time_stamp DATE)"""
cursor.execute(create_result_table)
create_question_table = """CREATE TABLE IF NOT EXISTS maths_questions(question_id INTEGER PRIMARY KEY, test_type TEXT,test_level TEXT, question TEXT, answer TEXT) """
cursor.execute(create_question_table)
db.commit()


def make_question(question_text, type, level, answer):
    question_type = ""
    question_level = ""
    if question_text:
        if type is 1:
            question_type = "Pure"
            if level is 1:
                if answer.isalnum() is True:
                    question_level = "AS"
                    insert_question = (
                        "INSERT INTO maths_questions(test_type, test_level, question,answer) VALUES (?, ?, ?, ?) ")
                    cursor.execute(insert_question, [(question_type),
                                                     (question_level), (question_text), (answer)])
                    db.commit()
                    return True
                else:
                    messagebox.showerror(
                        "Answer", "Answer cannot be left blank and no spaces in answer")
            elif level is 2:
                if answer.isalnum() is True:
                    question_level = "A2"
                    insert_question = (
                        "INSERT INTO maths_questions(test_type, test_level, question, answer) VALUES (?, ?, ?, ?) ")
                    cursor.execute(insert_question, [(question_type),
                                                     (question_level), (question_text), (answer)])
                    db.commit()
                    return True
                else:
                    messagebox.showerror(
                        "Answer", "Answer cannot be left blank and no spaces in answer")
            else:
                messagebox.showerror("Level", "Level cannot be left blank")
        elif type is 2:
            question_type = "Applied"
            if level is 1:
                if answer.isalnum() is True:
                    question_level = "AS"
                    insert_question = (
                        "INSERT INTO maths_questions(test_type, test_level, question, answer) VALUES (?, ?, ?, ?) ")
                    cursor.execute(insert_question, [(question_type),
                                                     (question_level), (question_text), (answer)])
                    db.commit()
                    return True
                else:
                    messagebox.showerror(
                        "Answer", "Answer cannot be left blank and no spaces in answer")
            elif level is 2:
                if answer.isalnum() is True:
                    question_level = "A2"
                    insert_question = (
                        "INSERT INTO maths_questions(test_type, test_level, question, answer) VALUES (?, ?, ?, ?) ")
                    cursor.execute(insert_question, [(question_type),
                                                     (question_level), (question_text), (answer)])
                    db.commit()
                    return True
                else:
                    messagebox.showerror(
                        "Answer", "Answer cannot be left blank and no spaces in answer")
            else:
                messagebox.showerror("Level", "Level cannot be left blank")
        else:
            messagebox.showerror("Type", "Type cannot be left blank")
    else:
        messagebox.showerror("Question", "Question cannot be left blank")


def start_loop(type, level):
    select_question = "SELECT question FROM maths_question WHERE test_type = ? AND test_level = ? "
