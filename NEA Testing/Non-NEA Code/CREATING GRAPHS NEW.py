def incorrect_graphs(user_id):
    dates_pure = []
    correct_pure = []
    dates_applied = []
    correct_applied = []
    sql_pure = "SELECT time_stamp,SUM(Incorrect) FROM pure_results WHERE user_id = ? GROUP BY time_stamp"
    sql_applied = "SELECT time_stamp, SUM(Incorrect) FROM applied_results WHERE user_id = ? GROUP BY time_stamp"
    cursor.execute(sql_pure, [(user_id)])
    for a in cursor.fetchall():
        dates_pure.append(a[0])
        correct_pure.append(a[1])
    cursor.execute(sql_applied, [(user_id)])
    for b in cursor.fetchall():
        dates_applied.append(b[0])
        correct_applied.append(b[1])
    if len(dates_pure) > len(dates_applied):
        plt.plot(dates_pure, correct_pure, label="Pure Progess")
        plt.plot(dates_applied, correct_applied, label="Applied Progess")
        plt.xlabel("Dates of Maths Question Attempted")
        plt.ylabel("Questions Incorrect")
        plt.title("Comparsion of Incorrect Progess")
        plt.legend()
        plt.show()
    elif len(dates_applied) > len(dates_pure):
        plt.plot(dates_applied,correct_applied, label="Applied Progess")
        plt.plot(dates_pure, correct_pure, label="Correct Progess")
        plt.xlabel("Dates of Maths Question Attempted")
        plt.ylabel("Questions Incorrect")
        plt.title("Comparsion of Incorrect Progess")
        plt.legend()
        plt.show()
    else:
        plt.plot(dates_pure, correct_pure, label="Pure Progess")
        plt.plot(dates_applied, correct_applied, label="Applied Progess")
        plt.xlabel("Dates of Maths Question Attempted")
        plt.ylabel("Questions Incorrect")
        plt.title("Comparsion of Incorrect Progess")
        plt.legend()
        plt.show()
