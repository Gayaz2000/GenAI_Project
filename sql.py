import sqlite3

# Connect to the database (creates it if it doesn't exist)
connections = sqlite3.connect("student.db")
Cursor = connections.cursor()

# SQL command to create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENTS(
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25)
)
"""
Cursor.execute(table_info)

# Insert data into the table
Cursor.execute("INSERT INTO STUDENTS VALUES ('Gayaz', 'MBA', 'A')")
Cursor.execute("INSERT INTO STUDENTS VALUES ('Ramana', 'Bsc', 'B')")
Cursor.execute("INSERT INTO STUDENTS VALUES ('Uma', 'Bsc', 'B')")
Cursor.execute("INSERT INTO STUDENTS VALUES ('Reshma', 'BTech', 'A')")

print("The inserted records are: ")

data = Cursor.execute('''SELECT * FROM STUDENTS;''')
for row in data :
    print(row)

