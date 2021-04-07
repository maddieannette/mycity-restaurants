import sqlite3
from sqlite3 import Error
import os

db_file = os.getcwd() + "/data-retrieve-app/sqlite.db"
conn = sqlite3.connect('sqlite.db')
c = conn.cursor()

# c.execute("""CREATE TABLE restaurants(
#             name TEXT,
#             rating INT,
#             numOfReviews INT,
#             longitude REAL, 
#             latitude REAL
#             )""")
# c.execute("INSERT INTO restaurants VALUES ('Red Lion Pub', '4.3', 267, 34.55353, 23423423)")
c.execute("SELECT * FROM restaurants WHERE name='Red Lion Pub'")
print(c.fetchone())

conn.commit()
conn.close()

# db_file = os.getcwd() + "/data-retrieve-app/sqlite.db"
# conn = None
# try:
#     conn = sqlite3.connect(db_file)
#     print(sqlite3.version)
# except Error as e:
#     print(e)
# finally:
#     if conn:
#         conn.close()







# def create_connection(db_file):
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except Error as e:
#         print(e)
#     # finally: 
#     #     if conn:
#     #         conn.close()
#     return conn



# def create_table(conn, create_table_sql):
#     try:
#         c = conn.cursor()
#         c.execute(create_table_sql)
#     except Error as e:
#         print(e)


# def main():
#     database = os.getcwd() + "/data-retrieve-app/sqlite.db"

# conn = create_connection(database)

# if conn is not None:
#     create_table(conn, sql_create_restaurants_table)
# else: 
#     ("Error! No database connection ")

# if __name__ == '__main__':
#     main()
    # create_connection(os.getcwd() + "/data-retrieve-app/sqlite.db")       
