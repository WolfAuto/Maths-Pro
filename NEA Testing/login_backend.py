import sqlite3 as sql
with sql.connect("Maths_Pro.db") as db:
    global cursor
    cursor = db.cursor()


def vaildate_account(username, password):
    find_user = ("SELECT * FROM personal_details WHERE username = ? AND password = ?")
    cursor.execute(find_user, [(username), (password)])
    checking = cursor.fetchall()
    print("Working now checking results")
    print(username)
    print(password)
    print(checking)

    if checking:
        for i in checking:
            print("Account Found")
            return True

    else:
        return False


def student_teacher(username):
    load_area = (
        "SELECT accounts.username ,  personal_deatils.School FROM accounts INNER JOIN personal_details USING(account_id) WHERE username = ?  ")

    cursor.execute(load_area, [(username), (school)])
    checking = cursor.fetchall()
    print("Checking whether user is a student or teacher")
    print(school)
