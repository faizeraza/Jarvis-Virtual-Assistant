import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="mfr754", database="db")


def getDATA(command, reply):
    mycursor = mydb.cursor()

    mycursor.execute("DESC messages")
    TABLES = mycursor.fetchall()
    for column in TABLES:
        print(column)



