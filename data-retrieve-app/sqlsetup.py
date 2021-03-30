import sqlite3
from sqlite3 import Error


db_file = os.getcwd() + "/data-retrieve-app/sqlite.db"
conn = None
try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
except Error as e:
    print(e)
finally:
    if conn:
        conn.close()
