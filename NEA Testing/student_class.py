import sqlite3 as sql

with sql.connect("updatedfile.db") as db:
    cursor = db.cursor()
