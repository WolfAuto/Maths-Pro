
from tkinter import messagebox
import datetime as dt
import random
from create_connection import cursor, cursor1, db

current_date = dt.date.today().strftime("%Y-%m-%d")
create_result_table = """CREATE TABLE IF NOT EXISTS maths_result(maths_id INTEGER PRIMARY KEY , score INTEGER, correct_pure INTEGER, correct_applied INTEGER, incorrect_pure INTEGER, incorrect_applied INTEGER, time_stamp DATE)"""
cursor.execute(create_result_table)
create_question_table = """CREATE TABLE IF NOT EXISTS maths_questions(question_id INTEGER PRIMARY KEY, test_type TEXT,test_level TEXT, question TEXT, answer TEXT) """
cursor.execute(create_question_table)
db.commit()

question_store = []


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


def query(level, type):
    sql = """ SELECT COUNT(question_id) FROM maths_questions WHERE test_type=? AND test_level = ?"""
    cursor.execute(sql, [(type), (level)])
    result = cursor.fetchone()
    return result[0]


def random_number(total):
    data = random.sample(range(1, total+1), 1)
    running = True

    while running:
        data = random.sample(range(1, total+1), 1)
        if (data[0] in question_store) is False:
            question_store.append(data[0])
            return data[0]
        elif (len(question_store)) is total:
            return "stop"
        else:
            pass


def get_question(self, type, level):
    query = "SELECT COUNT(question_id) FROM maths_questions WHERE test_type=? AND test_level=?"
    cursor.execute(query, [(type), (level)])
    row = cursor.fetchone()

    return random_num(row[0])


def actual_question(self, type, level):
    query = "SELECT question,answer FROM maths_question WHERE question_id=? AND test_type=? AND test_level=?"
    cursor.execute(query, [(self.get_question(type, level)), (type), (level)])
    row = cursor.fetchone()

    return row[0], row[1]


def end_loop(correct, incorrect, score, questions_wrong, total_questions):
    print("hello")
