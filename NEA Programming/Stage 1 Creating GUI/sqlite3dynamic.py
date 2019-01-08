import sqlite3
import random
conn = sqlite3.connect("test.db")
c = conn.cursor()

listfirst = ["john", "mary", "alice", "rias", "sam", "luke", "gerald"]
listsurname = ["Sky", "Mac", "Smith", "Snow", "Stark", "Jona", "Scarlet"]
listage = [18, 21, 49, 30, 25, 16, 17]
listclass = ["13C", "12A", "12B", "12C", "13L", "13D", "13A"]
listschool = ["Student", "Teacher"]
listuser = ["test1", "test2", "test3", "test4", "test5", "test6", "test7"]
listpassword = ["pass1", "pass2", "pass3", "pass4", "pass5", "pass6", "pass7"]


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS details(firstname TEXT , surname TEXT  , age INTEGER , class TEXT , school TEXT , username TEXT , password TEXT )")


def dynamic_entry():
    a = random.randrange(0, 6)
    b = random.randint(0, 1)
    c.execute("INSERT INTO details (firstname, surname, age , class, school, username, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (listfirst[a], listsurname[a], listage[a], listclass[a], listschool[b], listuser[a], listpassword[a]))
    conn.commit()


create_table()
for i in range(10):
    dynamic_entry()
c.close()
conn.close()
