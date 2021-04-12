import sqlite3
from sqlite3 import Error
import os
import main
from main import Place
from main import data_pull

db_file = os.getcwd() + "/data-retrieve-app/sqlite.db"
conn = sqlite3.connect('sqlite.db')
c = conn.cursor()

place = ' '
name = ' '
rating = 0
is_closed = 0
review_count = 0 
longitude = 0
latitude = 0

# c.execute('''DROP TABLE restaurants''')

c.execute("""CREATE TABLE IF NOT EXISTS restaurants(
            name TEXT,
            rating REAL,
            is_closed INT,
            review_count INT,
            longitude REAL, 
            latitude REAL
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )""")
# c.execute('''INSERT INTO restaurants(name, rating, is_closed, review_count, longitude, latitude) VALUES(?, ?, ?, ?, ?, ?)''', (name, rating, is_closed, review_count, longitude, latitude))
# c.execute("SELECT * FROM restaurants")


# print(c.fetchall())

# conn.commit()
# conn.close()