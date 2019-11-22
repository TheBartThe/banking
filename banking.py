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
    while True:
        firstName = input("Enter first name (max 50 characters): ").lower()
        if len(firstName) > 50:
            print("First name too long, please enter another")
            continue
        else:
            break
    while True:
        lastName = input("Enter surname (max 50 characters): ").lower()
        if len(lastName) > 50:
            print("Surname too long, please enter another")
            continue
        else:
            break
    while True:
        address = input("Enter home address (max 100 characters): ").lower()
        if len(address) > 100:
            print("Home address too long, please enter another")
            continue
        else:
            break
    while True:
        email = input("Enter email address (max 100 characters): ").lower()
        if len(email) > 100:
            print("Email address too long, please enter another")
            continue
        else:
            break
    while True:
        password = input("Enter password (max 50 characters): ")
        if len(password) > 50:
            print("Password is too long, please enter another")
            continue
        else:
            break
    try:
        with connection.cursor() as cursor:
            query = f"insert into customers (firstName, lastName, address, email, password) values ('{firstName}', '{lastName}', '{address}', '{email}', '{password}');"
            query2 = "insert into accounts (customerNumber) values (LAST_INSERT_ID());"
            cursor.execute(query)
            cursor.execute(query2)
        connection.commit()
        print("Thank you for creating an account with The Bank Of Vieran")
    finally:
        pass

def showData():
    try:
        with connection.cursor() as cursor:
            query = "select * from customers;"
            query2 = "select * from accounts;"
##            query = f"select * from customers where email = {email};"
##            query2 = "select * from accounts where accountNumber = LAST_INSERT_ID();"
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
