from create_connection import cursor, cursor1, db
import matplotlib.pyplot as plt

def graph_pure(user_id):
    global result
    result = []
    dates = []
    correct = []
    incorrect = []
    total_questions = []
    sql = "SELECT time_stamp,correct_pure,incorrect_pure,total_questions FROM pure_results WHERE user_id = ? ORDER BY time_stamp"
    cursor.execute(sql, [(user_id)])
    for row in cursor.fetchall():
        result.append(row)
    for data in range(0, len(result)-1):
        if result[data][0] == result[data+1][0]:
            print("same date")
        else:
            print("pass")



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
    plt.plot(dates_pure,correct_pure, label="Pure Progess")
    plt.plot(dates_applied,correct_applied, label="Applied Progress")
    plt.xlabel("Dates of Maths Question Attempted")
    plt.ylabel("Graph of Correct Progress")
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
    plt.plot(dates_pure,incorrect_pure, label="Incorrect Pure Progess")
    plt.plot(dates_applied,incorrect_applied, label="Incorrect Applied Progress")
    plt.xlabel("Dates of Maths Question Attempted")
    plt.ylabel("Graph of Incorrect Progress")
    plt.title("A Level Maths Incorrect Progress")
    plt.legend()
    plt.show()
def graph_total_questions(user_id):
    dates_pure= []
    total_questions_pure = []
    dates_applied= []
    total_questions_applied = []
    sql_pure = "SELECT time_stamp, total_questions FROM pure_results WHERE user_id = ? GROUP BY time_stamp"
    sql_applied = "SELECT time_stamp, score FROM applied_results WHERE user_id = ? GROUP BY time_stamp"

    cursor.execute(sql_pure, [(user_id)])
    for a in cursor.fetchall():
        dates_pure.append(a[0])
        total_questions.append(a[1])
    cursor.execute(sql_applied, [(user_id)])
    #for b
    
graph_total_questions(10)
