import sqlite3
from datetime import datetime, date

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(32), '
'surname VARCHAR(32), age INTEGER, city VARCHAR(32))')
cursor.execute('CREATE TABLE IF NOT EXISTS Courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(32),'
' time_start DATE, time_end DATE)')
cursor.execute('CREATE TABLE IF NOT EXISTS Student_courses (student_id INTEGER,'
' courses_id INTEGER, UNIQUE(student_id, courses_id))')

courses = [(1, 'python', str(date(2021, 7, 21)), str(date(2021, 8, 21))),
(2, 'java', str(date(2021, 7, 13)), str(date(2021, 8, 16)))]
students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
(3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
students_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

class Connector():

    def __init__(self):


cursor.executemany('INSERT OR IGNORE INTO Student_courses VALUES (?, ?)', students_courses)
conn.commit()
cursor.executemany('INSERT OR IGNORE INTO Courses VALUES (?, ?, ?, ?)', courses)
conn.commit()
cursor.executemany('INSERT OR IGNORE INTO Students VALUES (?, ?, ?, ?, ?)', students)
conn.commit()
cursor.execute('SELECT * FROM Students WHERE age > 30')
print(cursor.fetchall())
cursor.execute('SELECT * FROM Student_courses WHERE courses_id = 1')
rows = cursor.fetchall()

for row in rows:
    cursor.execute('SELECT * FROM Students WHERE id = ?', row)
conn.close()