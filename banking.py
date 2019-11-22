from pymysql import connect
import os

connection = connect(
    host = os.getenv("MYSQL_HOST"),
    user = os.getenv("MYSQL_USER"),
    password = os.getenv("MYSQL_PASSWORD"),
    db = os.getenv("MYSQL_DATABASE"),
    charset = "utf8mb4"
    )

def newCustomer():
    firstName = input("Enter first name: ").lower()
    lastName = input("Enter surname: ").lower()
    address = input("Enter homer address: ").lower()
    email = input("Enter email address: ").lower()
    password = input("Enter password: ")
    try:
        with connection.cursor() as cursor:
            query = "insert into customers (firstName, lastName, address, email, password) values ('Jenny', 'Taylor', '43 Home Avenue', 'jennay@yahoo.com', 'lol123');"
            query2 = "insert into accounts (customerNumber) values (LAST_INSERT_ID());"
            cursor.execute(query)
            cursor.execute(query2)
        connection.commit()
    finally:
        pass

def showData():
    try:
        with connection.cursor() as cursor:
            query = "select * from customers;"
            query2 = "select * from accounts;"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.execute(query2)
            result2 = cursor.fetchall()
            print(result)
            print(result2)
    finally:
        pass

newCustomer()
showData()

connection.close()
