import json
import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    user = "root",
    password = "cars",
    host = "localhost",
    database = "cars_database",
    port = 3306
    )

con = connection_pool.get_connection()
cursor = con.cursor()

# mysql database navigation
if con.is_connected():
    # database info
    db_Info = con.get_server_info()
    print("Connected to MySQL database using connection pool ... MySQL Server version on ",db_Info)

    # show database connection
    cursor.execute("select database();")
    record = cursor.fetchone()
    print ("Your connected to - ", record)

    # CREATE TABLE
    # cursor.execute("CREATE TABLE cars (id INT AUTO_INCREMENT PRIMARY KEY, car VARCHAR(255), color VARCHAR(255))")

    # DELETE TABLE
    # cursor.execute("DROP TABLE cars")

    # INSERT ITEM
    # cursor.execute("INSERT INTO cars(car, color) VALUES('Car A', 'blue')")
    # cursor.execute("INSERT INTO cars(car, color) VALUES('Car B', 'red')")
    # cursor.execute("INSERT INTO cars(car, color) VALUES('Car C', 'red')")
    # cursor.execute("INSERT INTO cars(car, color) VALUES('Car D', 'blue')")
    # cursor.execute("INSERT INTO cars(car, color) VALUES('Car E', 'blue')")
    # con.commit()
    # for row in cursor:
    #     print(row)

    # DELETE ITEM
    # cursor.execute("DELETE FROM cars WHERE id=2")
    # con.commit()
    # print(cursor.rowcount, "items currently in the cars table")

    # # SHOW TABLES
    # cursor.execute("SHOW TABLES")
    # for tables in cursor:
    #     print("The existing tables in the database are:")
    #     print(tables)

    # # SHOW ROWS
    # cursor.execute("SELECT * FROM cars")
    # print(f"The contents of the {tables} table are:")
    # for rows in cursor:
    #     print(rows)

# SHOW TABLES
cursor.execute("SHOW TABLES")
for tables in cursor:
    print("The existing tables in the database are:")
    print(tables)

cursor.execute("SELECT * FROM cars")
print(f"The contents of the {tables} table are:")
for rows in cursor:
    print(rows)

def get_blue_cars(car: str, con):
    # query = "SELECT color FROM cars WHERE car=%s"
    cursor.execute("SELECT color FROM cars WHERE car=%s", (car, con))
    row = cursor.fetchone()
    return row[2]

my_car = get_blue_cars("Car A", con)
print(my_car)

# def get_red_cars(car: str):
#     query = "SELECT color FROM cars WHERE car = %s"
#     cur = get_cursor()
#     with cur:
#         cur.execute(query, (car))
#         row = cur.fetchone()
#         return row[0]
