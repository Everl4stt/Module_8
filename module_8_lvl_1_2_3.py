import sqlite3
from datetime import datetime, date

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS Students (id int primary key, name varchar(32), '
'surname varchar(32), age int, city varchar(32))')
cursor.execute('CREATE TABLE IF NOT EXISTS Courses (id int primary key, name varchar(32),'
' time_start date, time_end date)')
cursor.execute('CREATE TABLE IF NOT EXISTS Student_courses (student_id references Students(id),'
' courses_id references Courses(id))')

courses = ([1, 'python', str(date(2021, 7, 21)), str(date(2021, 8, 21))],
[2, 'java', str(date(2021, 7, 13)), str(date(2021, 8, 16))])
students = ([1, 'Max', 'Brooks', 24, 'Spb'], [2, 'John', 'Stones', 15, 'Spb'],
[3, 'Andy', 'Wings', 45, 'Manchester'], [4, 'Kate', 'Brooks', 34, 'Spb'])
students_courses = ([1, 1], [2, 1], [3, 1], [4, 2])
cursor.executemany('INSERT OR REPLACE INTO Courses VALUES (?, ?, ?, ?)', courses)
cursor.executemany('INSERT OR REPLACE INTO Students VALUES (?, ?, ?, ?, ?)', students)
cursor.executemany('INSERT OR REPLACE INTO Student_courses VALUES (?, ?)', students_courses)
conn.commit()
cursor.execute('SELECT * FROM Students WHERE age > 30')
print(cursor.fetchall())
cursor.execute('SELECT * FROM Student_courses WHERE courses_id == 1')
print(cursor.fetchall())
