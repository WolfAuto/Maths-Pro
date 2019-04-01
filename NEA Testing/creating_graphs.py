from create_connection import cursor, cursor1, db
from questions_results import get_student
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use(["bmh", "seaborn-talk"])


def graph_correct(user_id):
    dates_pure = []
    correct_pure = []
    dates_applied = []
    correct_applied = []
    sql_pure = "SELECT time_stamp,sum(correct_pure) FROM pure_results WHERE user_id = ? GROUP BY time_stamp"
    sql_applied = "SELECT time_stamp, sum(correct_applied) FROM applied_results WHERE user_id = ? GROUP BY time_stamp"

    cursor.execute(sql_pure, [(user_id)])
    for a in cursor.fetchall():
        dates_pure.append(a[0])
        correct_pure.append(a[1])
    cursor.execute(sql_applied, [(user_id)])
    for b in cursor.fetchall():
        dates_applied.append(b[0])
        correct_applied.append(b[1])

    print(dates_pure)
    print(dates_applied)
    print(correct_pure)
    print(correct_applied)
    plt.plot(dates_pure, correct_pure, label="Pure Progess")
    plt.plot(dates_applied, correct_applied, label="Applied Progress")
    plt.xlabel("Dates of Maths Question Attempted")
    plt.ylabel("Questions Correct")
    plt.title("A Level Maths Correct Progress")
    plt.legend()
    plt.show()


def graph_incorrect(user_id):
    dates_pure = []
    incorrect_pure = []
    dates_applied = []
    incorrect_applied = []
    sql_pure = "SELECT time_stamp,sum(incorrect_pure) FROM pure_results WHERE user_id = ? GROUP BY time_stamp"
    sql_applied = "SELECT time_stamp, sum(incorrect_applied) FROM applied_results WHERE user_id = ? GROUP BY time_stamp"

    cursor.execute(sql_pure, [(user_id)])
    for a in cursor.fetchall():
        dates_pure.append(a[0])
        incorrect_pure.append(a[1])
    cursor.execute(sql_applied, [(user_id)])
    for b in cursor.fetchall():
        dates_applied.append(b[0])
        incorrect_applied.append(b[1])

    print(dates_pure)
    print(dates_applied)
    print(incorrect_pure)
    print(incorrect_applied)
    plt.plot(dates_pure, incorrect_pure, label="Incorrect Pure Progess")
    plt.plot(dates_applied, incorrect_applied, label="Incorrect Applied Progress")
    plt.xlabel("Dates of Maths Question Attempted")
    plt.ylabel("Incorrect Questions")
    plt.title("A Level Maths Incorrect Progress")
    plt.legend()
    plt.show()


def graph_total_questions(user_id):
    dates = []
    total_questions = []

    sql = "SELECT time_stamp,sum(total_questions) total FROM (select time_stamp,total_questions FROM pure_results WHERE user_id = ? UNION ALL SELECT time_stamp,total_questions FROM applied_results WHERE user_id = ?) t GROUP BY time_stamp"
    cursor.execute(sql, [(user_id), (user_id)])
    for a in cursor.fetchall():
        dates.append(a[0])
        total_questions.append(a[1])
    plt.plot(dates, total_questions)
    plt.xlabel("Dates of Questions Attempted")
    plt.ylabel("Total Questions Attempted")
    plt.title("A Level Maths Total Questions Attempted")
    plt.show()


def total_score(user_id):
    sql = "SELECT sum(score) total FROM (select score FROM pure_results WHERE user_id = ? UNION ALL SELECT score FROM applied_results WHERE user_id = ?) t "
    resp = pd.read_sql_query(sql, db, params=(user_id, user_id,))
    if resp.empty:
        return "No Score Attempt"
    else:
        return resp
total_score(10)
