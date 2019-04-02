import pandas as pd
from tkinter import messagebox
import datetime as dt
import random

from create_connection import cursor, cursor1, db

current_date = dt.date.today().strftime("%Y-%m-%d")
create_pure_table = """CREATE TABLE IF NOT EXISTS pure_results(maths_id INTEGER PRIMARY KEY, user_id INTEGER, level TEXT , score INTEGER ,total_questions INTEGER, Correct INTEGER, Incorrect INTEGER,  time_stamp DATE, FOREIGN KEY (user_id) REFERENCES Students(ID))"""
create_applied_table = """CREATE TABLE IF NOT EXISTS applied_results(maths_id INTEGER PRIMARY KEY, user_id INTEGER, level TEXT , score INTEGER ,total_questions INTEGER,  Correct INTEGER, Incorrect INTEGER, time_stamp DATE,FOREIGN KEY (user_id) REFERENCES Students(ID))"""
cursor.execute(create_pure_table)
cursor.execute(create_applied_table)
create_question_table = """CREATE TABLE IF NOT EXISTS maths_questions(question_id INTEGER PRIMARY KEY, test_type TEXT,test_level TEXT, question TEXT, answer TEXT) """
cursor.execute(create_question_table)
db.commit()

question_store = []
questions = []
question_answers = []


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
                                                     (question_level), (question_text), (str(answer))])
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
                                                     (question_level), (question_text), (str(answer))])
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
                                                     (question_level), (question_text), (str(answer))])
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
                                                     (question_level), (question_text), (str(answer))])
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


def random_num(total):
    data = random.sample(range(total), 1)
    running = True

    while running:
        data = random.sample(range(total), 1)
        if (data[0] in question_store) is False:
            question_store.append(data[0])
            return data[0]
        elif (len(question_store)) is total:
            return "stop"
        else:
            pass


def get_question(type, level):
    query = "SELECT question,answer FROM maths_questions WHERE test_type = ? AND test_level = ?"
    resp = pd.read_sql_query(query, db, params=[(type), (level)])

    query1 = "SELECT COUNT(question_id) FROM maths_questions WHERE test_type=? AND test_level=?"
    cursor1.execute(query1, [(type), (level)])
    total = cursor1.fetchone()[0]
    rand_num = random_num(total)
    if rand_num is not "stop":
        return [resp["question"][rand_num], resp["Answer"][rand_num]]
    else:
        return ["No more Questions", "END"]


def compare_answers(user_input, actual_answer):
    if user_input.find(",") is not -1:
        mylist = user_input.split(",")
        mylist.sort(key=int)
        user_input = ",".join(mylist)
        if str(user_input) == str(actual_answer):
            return True
        else:
            return False
    else:
        if str(user_input) == str(actual_answer):
            return True
        else:
            return False


def get_student(username):
    sql = "SELECT ID FROM Students WHERE username = ? "
    cursor.execute(sql, [(username)])
    return cursor.fetchone()[0]


def end_loop(loop, user, correct, incorrect, score, level, total):
    if total == 0:
        return False
    else:
        store_id = get_student(user)
        total = len(question_store)
        if loop is "Pure":
            sql = "INSERT INTO pure_results (user_id,level, score, correct_pure, incorrect_pure,total_questions, time_stamp) VALUES (?, ?, ?, ?, ?, ?,?) "
            cursor.execute(sql, [(store_id), (level), (score), (correct),
                                 (incorrect), (total), (current_date)])
            db.commit()
            question_store.clear()
            return True

        elif loop is "Applied":
            sql = "INSERT INTO applied_results (user_id,level, score, correct_applied, incorrect_applied,total_questions, time_stamp) VALUES (?, ?, ?, ?, ?, ?,?) "
            cursor.execute(sql, [(store_id), (level), (score), (correct),
                                 (incorrect), (total), (current_date)])
            db.commit()
            question_store.clear()
            return True
