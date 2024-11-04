import sqlite3
from datetime import date

class DataBase():
    connection = None

    def __init__(self, db_name):
        self.db_name = db_name
        if self.connection == None:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        print(f'Соединение с базой данных {self.db_name} установленно')

    def execute(self, query, param = ()):
        self.cursor.execute(query, param)
        self.connection.commit()
        return self.cursor

    def close(self):
        self.connection.close()
        print(f'Соединение с базой данных {self.db_name} закрыто')

class DataBaseModels():
    params = {}

    def __init__(self, *args, **kwargs):
        self.data = args

    @classmethod
    def db_name(cls):
        return cls.__name__.lower()

    @classmethod
    def set_db(cls, db):
        cls.database = DataBase(db)

    @classmethod
    def create_table(cls):
        attributes = ', '.join([f'{name} {atrtype}' for name, atrtype in cls.params.items()])
        query = f'CREATE TABLE IF NOT EXISTS {cls.db_name()} ({attributes});'
        cls.database.execute(query)

    def save_data(self):
        keys = ', '.join(self.params.keys())
        values = ', '.join(['?'] * len(self.data))
        query = f'INSERT OR IGNORE INTO {self.db_name()} ({keys}) VALUES ({values});'
        self.database.execute(query, tuple(self.data))

    @classmethod
    def show_data(cls):
        query = f'SELECT * FROM {cls.db_name()};'
        print(f'Данные из базы {cls.db_name()}: ', end = '')
        return cls.database.execute(query).fetchall()

    @classmethod
    def insert(cls, **filters):
        print('Результаты поиска:')
        conditions = []
        values = []
        for field, condition in filters.items():
            if isinstance(condition, tuple):
                operation, value = condition
                conditions.append(f'{field} {operation} ?')
                values.append(value)
            else:
                conditions.append(f'{field} = ?')
                values.append(condition)
        manyconditions = ' AND '.join(conditions)
        query = f'SELECT * FROM {cls.db_name()} WHERE {manyconditions};'
        return cls.database.execute(query, tuple(values)).fetchall()

class Students(DataBaseModels):
    params = {
        'id' : 'INTEGER PRIMARY KEY',
        'name' : 'VARCHAR(32)',
        'surname': 'VARCHAR(32)',
        'age' : 'INT',
        'city' : 'VARCHAR(32)'
    }

class Courses(DataBaseModels):
    params = {
        'id' : 'INTEGER PRIMARY KEY',
        'name' : 'VARCHAR(32)',
        'time_start': 'DATE',
        'time_end' : 'DATE',
    }

class StudentsCourses(DataBaseModels):
    params = {
        'id' : 'INTEGER PRIMARY KEY',
        'id_students' : 'INTEGER REFERENCES students(id)',
        'id_courses': 'INTEGER REFERENCES courses(id)',
    }



if __name__ == '__main__':
    courses = [(1, 'python', str(date(2021, 7, 21)), str(date(2021, 8, 21))),
               (2, 'java', str(date(2021, 7, 13)), str(date(2021, 8, 16)))]
    students_base = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
                     (3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
    students_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]
    mydb = DataBase('mydb.sqlite')
    Students.set_db('mydb.sqlite')
    Students.create_table()
    student1 = Students(1, 'Max', 'Brooks', 24, 'Spb')
    student1.save_data()
    student2 = Students(2, 'John', 'Stones', 15, 'Spb')
    student2.save_data()
    student3 = Students(3, 'Andy', 'Wings', 45, 'Manchester')
    student3.save_data()
    student4 = Students(4, 'Kate', 'Brooks', 34, 'Spb')
    student4.save_data()
    print(Students.show_data())
    print(Students.insert(age = ('>', 20), city = 'Spb'))
    Courses.set_db('mydb.sqlite')
    Courses.create_table()
    courses1 = Courses(1, 'python', str(date(2021, 7, 21)), str(date(2021, 8, 21)))
    courses1.save_data()
    courses2 = Courses(2, 'java', str(date(2021, 7, 13)), str(date(2021, 8, 16)))
    courses2.save_data()
    print(Courses.show_data())
    StudentsCourses.set_db('mydb.sqlite')
    StudentsCourses.create_table()
    sc1 = StudentsCourses(1, 1, 1)
    sc1.save_data()
    sc2 = StudentsCourses(2, 2, 1)
    sc2.save_data()
    sc3 = StudentsCourses(3, 3, 1)
    sc3.save_data()
    sc4 = StudentsCourses(4, 4, 2)
    sc4.save_data()
    print(StudentsCourses.show_data())
    for results in StudentsCourses.insert(id_courses = 1):
        print(Students.insert(id = list(results)[1], city = 'Spb'))
    mydb.close()