import sqlite3
from datetime import datetime, date

courses = [(1, 'python', str(date(2021, 7, 21)), str(date(2021, 8, 21))),
(2, 'java', str(date(2021, 7, 13)), str(date(2021, 8, 16)))]
students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
(3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
students_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

class DataBase():

    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Students (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(32), '
                       'surname VARCHAR(32), age INTEGER, city VARCHAR(32))')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(32),'
                       ' time_start DATE, time_end DATE)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Student_courses (student_id INTEGER,'
                       ' courses_id INTEGER, UNIQUE(student_id, courses_id))')
        print('База данных создана')

    def insert_students_courses(self, students_courses):
        self.cursor.executemany('INSERT OR IGNORE INTO Student_courses VALUES (?, ?)', students_courses)
        print('Данные о курсах, которые проходят студенты записаны')
        self.conn.commit()

    def insert_course(self, courses):
        self.cursor.executemany('INSERT OR IGNORE INTO Courses VALUES (?, ?, ?, ?)', courses)
        print('Данные о курсах записаны')
        self.conn.commit()

    def insert_students(self, students):
        self.cursor.executemany('INSERT OR IGNORE INTO Students VALUES (?, ?, ?, ?, ?)', students)
        print('Данные о студентах записаны')
        self.conn.commit()

    def select_students_age(self, *args):
        self.cursor.execute('SELECT * FROM Students WHERE age > ?', args)
        return self.cursor.fetchall()

    def select_students_from_courses(self, *args):
        self.cursor.execute('SELECT * FROM Student_courses WHERE courses_id = 1')
        rows = self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
        print('Подключение закрыто')

data = DataBase()
data.insert_students(students)
print(data.select_students_age(40))
