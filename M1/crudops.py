""" Playing with MySQL"""
import mysql.connector as mysql

# Connect to DB
mydb = mysql.connect(
    host="localhost",
    user="root",
    passwd="Gn2g8tawii#23",
    database="testdb"
)

mycursor = mydb.cursor(buffered=True) # Use buffered = True to prevent FetchOne issues

# mycursor.execute("CREATE DATABASE testdb") 

# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE TABLE STUDENTS (name VARCHAR(255), age INTEGER(10))")

# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Bob", 12),
            ("Amanda", 32),
            ("Jacob", 21),
            ("Avi", 18),
            ("Michelle", 52)
]

# mycursor.execute(sqlFormula, student1) # For one use executemany for list
# mycursor.executemany(sqlFormula, students)

mycursor.execute("SELECT * FROM students")

# myresult = mycursor.fetchall()
myresult1 = mycursor.fetchone() # retrieve just one entry
print(myresult1)

# for row in myresult:
#     print(row)

sql = "SELECT * FROM students WHERE age >=21"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(myresult)

sql = "UPDATE students SET age = 13 WHERE name = %s"

mycursor.execute(sql, ("Bob", ))

sql = "ALTER TABLE students ADD COLUMN location VARCHAR(255)" #Add Column
mycursor.execute(sql)

# Save
mydb.commit()
