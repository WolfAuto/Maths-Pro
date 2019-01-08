import random
import sqlite3
with sqlite3.connect("datalearn.db") as db:
    cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS details(userID INTEGER PRIMARY KEY, firstname VARCHAR(30) NOT NULL, surname VARCHAR(30) NOT NULL , age INTEGER NOT NULL, class VARCHAR(3) NOT NULL, school VARCHAR(20) NOT NULL, username VARCHAR(20) NOT NULL, password VARCHAR(20) NOT NULL);")
cursor.execute("INSERT INTO details(firstname,surname,age,class,school,username,password)VALUES('testname','name',21,'12D','Student','test_user','test_password')")
db.commit()

listfirst = ["john", "mary", "alice", "rias", "sam", "luke", "gerald"]
listsurname = ["Sky", "Mac", "Smith", "Snow", "Stark", "Jona", "Scarlet"]
listage = [18, 21, 49, 30, 25, 16, 17]
listclass = ["13C", "12A", "12B", "12C", "13L", "13D", "13A"]
listschool = ["Student", "Teacher"]
listuser = ["test1", "test2", "test3", "test4", "test5", "test6", "test7"]
listpassword = ["pass1", "pass2", "pass3", "pass4", "pass5", "pass6", "pass7"]


def dynamic_entry():
    a = random.randint(0, 6)
    b = random.randint(0, 1)
    first= str(listfirst[a])
    surname = str(listsurname[a])
    age= int(listage[a])
    clas = str(listclass[a])
    school = str(listschool[b])
    user = str(listuser[a])
    passw = str(listpassword[a])
    cursor.execute("INSERT INTO details(firstname, surname, age , class, school, username, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (first, surname, age, clas, school, user, passw))
for i in range(10):
    dynamic_entry()
cursor.close()
db.close()
