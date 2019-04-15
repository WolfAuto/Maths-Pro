from create_connection import cursor, cursor1, db
from questions_results import get_student
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
plt.style.use(["bmh", "seaborn-talk"])


def correct_graphs(user_id):
    dates_pure = []
    correct_pure = []
    sql_pure = """SELECT time_stamp,SUM(Correct) FROM pure_results
                WHERE user_id = ? GROUP BY time_stamp"""
    cursor.execute(sql_pure, [(user_id)])
    for a in cursor.fetchall():
        dates_pure.append(a[0])
        correct_pure.append(a[1])
    dates_applied = []
    correct_applied = []
    sql_applied = """SELECT time_stamp, SUM(Correct) FROM applied_results
                    WHERE user_id = ? GROUP BY time_stamp"""
    cursor.execute(sql_applied, [(user_id)])
    for b in cursor.fetchall():
        dates_applied.append(b[0])
        correct_applied.append(b[1])

    plt.figure(1)
    plt.subplot(211)
    plt.plot(dates_pure,correct_pure)
    plt.ylabel("Questions Correct")
    plt.xlabel("Dates of Maths Question Attempted")

    plt.title("Pure Maths Correct Progress")

    plt.subplot(212)
    plt.plot(dates_applied, correct_applied, "-g")
    plt.xlabel("Dates of Maths Question Attempted")
    plt.ylabel("Questions Correct")
    plt.title("Applied Maths Correct Progress")

    plt.tight_layout()

    plt.show()
def incorrect_graphs(user_id):
    dates_pure = []
    incorrect_pure = []
    dates_applied = []
    incorrect_applied = []
    sql_pure = """SELECT time_stamp,SUM(Incorrect) FROM pure_results
                WHERE user_id = ? GROUP BY time_stamp"""
    sql_applied = """SELECT time_stamp, SUM(Incorrect) FROM applied_results
                    WHERE user_id = ? GROUP BY time_stamp"""
    cursor.execute(sql_pure, [(user_id)])
    for a in cursor.fetchall():
        dates_pure.append(a[0])
        incorrect_pure.append(a[1])
    cursor.execute(sql_applied, [(user_id)])
    for b in cursor.fetchall():
        dates_applied.append(b[0])
        incorrect_applied.append(b[1])

    plt.figure(1)
    plt.subplot(211)
    plt.plot(dates_pure,incorrect_pure)
    plt.ylabel("Questions Incorrect")
    plt.xlabel("Dates of Maths Question Attempted")

    plt.title("Pure Maths Incorrect Progress")

    plt.subplot(212)
    plt.plot(dates_applied, incorrect_applied, "-g")
    plt.xlabel("Dates of Maths Question Attempted")
    plt.ylabel("Questions Incorrect")
    plt.title("Applied Maths Incorrect Progress")

    plt.tight_layout()

    plt.show()

def total_graph_correct(user_id):
    dates = []
    correct = []
    sql = """SELECT time_stamp,SUM(Correct) total FROM
(SELECT time_stamp,Correct FROM pure_results WHERE user_id = ?
UNION ALL SELECT time_stamp, Correct FROM applied_results WHERE user_id = ?)
t GROUP BY time_stamp"""
    cursor.execute(sql, [(user_id), (user_id)])
    for a in cursor.fetchall():
        dates.append(a[0])
        correct.append(a[1])
    print(dates)
    print(correct)
    plt.plot(dates, correct, label="Total Correct Progress")
    plt.xlabel("Dates of Maths Question Attempted")
    plt.ylabel("Questions Correct")
    plt.title("A Level Maths Total Correct Progress")
    plt.show()


def total_graph_incorrect(user_id):
    dates = []
    incorrect = []
    sql = """SELECT time_stamp,SUM(Incorrect) total
FROM (SELECT time_stamp,Incorrect FROM pure_results WHERE user_id = ?
UNION ALL SELECT time_stamp, Incorrect FROM applied_results WHERE user_id = ?)
t GROUP BY time_stamp"""
    cursor.execute(sql, [(user_id), (user_id)])
    for a in cursor.fetchall():
        dates.append(a[0])
        incorrect.append(a[1])
    plt.plot(dates, incorrect, label="Incorrect Progess")
    plt.xlabel("Dates of Maths Question Attempted")
    plt.ylabel("Incorrect Questions")
    plt.title("A Level Maths Total Incorrect Progress")
    plt.show()


def graph_total_questions(user_id):
    dates = []
    total_questions = []

    sql = """SELECT time_stamp,SUM(total_questions) total
FROM (SELECT time_stamp,total_questions
FROM pure_results WHERE user_id = ?
UNION ALL SELECT time_stamp,total_questions
FROM applied_results WHERE user_id = ?) t GROUP BY time_stamp"""
    cursor.execute(sql, [(user_id), (user_id)])
    for a in cursor.fetchall():
        dates.append(a[0])
        total_questions.append(a[1])
    plt.plot(dates, total_questions)
    plt.xlabel("Dates of Questions Attempted")
    plt.ylabel("Total Questions Attempted")
    plt.title("A Level Maths Total Questions Attempted")
    plt.show()


def score_graph(user_id):
    dates = []
    total_score = []
    sql = """SELECT time_stamp,SUM(score) total FROM
(SELECT time_stamp,score FROM pure_results WHERE user_id = ? UNION ALL SELECT time_stamp,score
FROM applied_results WHERE user_id = ?) t GROUP BY time_stamp"""
    cursor.execute(sql, [(user_id), (user_id)])
    for a in cursor.fetchall():
        dates.append(a[0])
        total_score.append(a[1])
    plt.plot(dates, total_score)
    plt.xlabel("Date")
    plt.ylabel("Current Score")
    plt.title("A level Score Progess")
    plt.show()


def total_score(user_id):
    sql = """SELECT SUM(score) total FROM
(SELECT score FROM pure_results WHERE user_id = ?
UNION ALL SELECT score FROM applied_results WHERE user_id = ?) t """
    resp = pd.read_sql_query(sql, db, params=[(user_id), (user_id)])
    if resp["total"][0] is None:
        return "No Score"
    else:
        return resp.to_csv(None, header = False, index = False)
