import mysql.connector

# connect to mysql server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)