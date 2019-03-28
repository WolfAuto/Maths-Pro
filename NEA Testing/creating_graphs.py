from create_connection import cursor, cursor1, db


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


def graph_correct_pure(user_id):
    global result
    result = []
    dates = []
    correct = []
    sql = "SELECT time_stamp,(correct_pure) FROM pure_results WHERE user_id = ?"
    value = 0
    cursor.execute(sql, [(user_id)])
    for row in cursor.fetchall():
        result.append(row)
    for data in range(0, len(result)-1):
        if result[data][0] == result[data+1][0]:
            value = value + (result[data][1] + result[data+1][1])
        else:
            correct.append(value)
            value = 0
    print("Dates")
    print(dates)
    print("Correct")
    print(correct)
def graph_correct(user_id):
    global result
    result = []
    sql = "SELECT time_stamp,sum(correct_pure) FROM pure_results WHERE user_id = ? GROUP BY time_stamp"
    cursor.execute(sql, [(user_id)])
    for row in cursor.fetchall():
        result.append(row)
graph_correct(8)
