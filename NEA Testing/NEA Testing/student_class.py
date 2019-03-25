from create_connection import cursor


def get_students():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students """
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def sort_age():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY Age ASC """
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def sort_surname():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY Surname"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def sort_class():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY class """
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def sort_forename():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY Forename"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def sort_gender():
    sql = """ SELECT ID, Forename, Surname, Age, class, gender FROM students ORDER BY Gender"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
