import mysql.connector

def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pythoncourse",
            database="school"
        )
        print("connected")
        return connection
    except Exception as e:
        print("Error:", e)

asd = connect()
print("asd")