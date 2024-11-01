# import sqlite3
# from datetime import datetime, date
#
# courses = [(1, 'python', str(date(2021, 7, 21)), str(date(2021, 8, 21))),
# (2, 'java', str(date(2021, 7, 13)), str(date(2021, 8, 16)))]
# students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
# (3, 'Andy', 'Wings', 45, 'Manchester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
# students_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]
#
# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
# class Database(metaclass = Singleton):
#     conn = None
#     def connect(self, db_name = None):
#         if self.conn == None:
#             self.conn = sqlite3.connect(db_name)
#             self.cursor = self.conn.cursor()
#         return self.cursor
#
#     def execute(self, query, params=()):
#         self.cursor.execute(query, params)
#         self.conn.commit()
#         return self.cursor
#
#     def close(self):
#         self.conn.close()
#
# class TableModel():
#     _fields = None
#
#     def __init__(self, **kwargs):
#         self._data = kwargs
#
#     @classmethod
#     def table_name(cls):
#         return cls.__name__.lower()
#
#     def create_table(cls):
#         atr = ", ".join([f"{name} {ftype}" for name, ftype in cls._fields.items()])
#         query = f"CREATE TABLE IF NOT EXISTS {cls.table_name()} ({atr});"
#         cls._db.execute(query)
#
#     def set_db(cls, db):
#         cls._db = db
#
#     def save(self):
#         keys = ", ".join(self._data.keys())
#         values = ", ".join(["?"] * len(self._data))
#         query = f"INSERT INTO {self.table_name()} ({keys}) VALUES ({values})"
#         self._db.execute(query, tuple(self._data.values()))
#
#     def select_all(cls):
#         query = f"SELECT * FROM {cls.table_name()}"
#         rows = cls._db.execute(query).fetchall()
#         return [cls(**dict(zip(cls._fields.keys(), row))) for row in rows]
#
#
# class StudentsDataBase(TableModel):
#     _fields = {
#         'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
#         'name': 'VARCHAR(32)',
#         'surname': 'VARCHAR(32)',
#         'age': 'INTEGER',
#         'city': 'VARCHAR(32)'}
#
#     def __init__(self, id = None, name = None, surname = None, age = None, city = None):
#         super().__init__(id = id, name = name, surname = surname, age = age, city = city)
#
#
# db = Database()
# student1 = StudentsDataBase(1, 'Max', 'Brooks', 24, 'Spb')
# student1.select_all()
#
#
#
#
#
