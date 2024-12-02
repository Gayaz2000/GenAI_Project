import sqlite3

# Connect to the database (creates it if it doesn't exist)
connections = sqlite3.connect("student.db")
cursor = connections.cursor()

# SQL command to create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENTS(
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25)
)
"""
cursor.execute(table_info)

# Insert data into the table
cursor.execute("INSERT INTO STUDENTS VALUES ('Gayaz', 'MBA', 'A')")
cursor.execute("INSERT INTO STUDENTS VALUES ('Ramana', 'B.sc', 'B')")
cursor.execute("INSERT INTO STUDENTS VALUES ('Uma', 'B.sc', 'B')")
cursor.execute("INSERT INTO STUDENTS VALUES ('Reshma', 'B.Tech', 'A')")

print("The inserted records are: ")

data = cursor.execute('''select * from student''')

# Commit changes and close the connection
connections.commit()
connections.close()
