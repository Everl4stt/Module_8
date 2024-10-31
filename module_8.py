import sqlite3
from datetime import datetime, date

from module_8_lvl_1_2_3 import StudentsDataBase

courses = [(1, 'python', str(date(2021, 7, 21)), str(date(2021, 8, 21))),
(2, 'java', str(date(2021, 7, 13)), str(date(2021, 8, 16)))]
students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
(3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
students_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

class DataBase():
    connection = None

    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        if self.connection == None:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        print(f'Соединение с базой данных {self.db_name} установленно')
        return self.cursor

    def execute(self, query, param = None):
        self.cursor.execute(query)
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
        cls.db = DataBase(db)

    @classmethod
    def create_table(cls):
        attributes = ', '.join([f'{name} {atrtype}' for name, atrtype in cls.params.items()])
        query = f'CREATE TABLE IF NOT EXIST {cls.db_name} ({attributes})'
        cls.db.execute(query = query)

    def save_data(self):
        keys = ', '.join(self.data.keys())
        values = ' '.join(['?'] * len(self.data))
        query = f'INSERT OR IGNORE INTO {self.db_name} ({keys}) VALUES ({values})'
        self.db.execute(query, tuple(self.data.values()))

    @classmethod
    def show_data(cls):
        query = f'SELECT * FROM {cls.db_name()}'
        return cls.db.execute(query).fetchall()

    @classmethod
    def insert(cls):
        pass

class Students(DataBaseModels):
    params = {
        'id' : 'INTEGER PRIMARY KEY',
        'name' : 'VARCHAR(32)',
        'surname': 'VARCHAR(32)',
        'age' : 'INT',
        'city' : 'VARCHAR(32)'
    }

    #def __init__(self, id = None, name = None, surname = None, age = None, city = None):



mydb = DataBase('mydb.sqlite')
mydb.connect()
StudentsDataBase.set_db('mydb.sqlite')
student1 = Students(1, 'Max', 'Brooks', 24, 'Spb')
Students.create_table()
Students.show_data()
student1.save_data()
Students.show_data()
