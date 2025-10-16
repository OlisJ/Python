import sqlite3

connention= sqlite3.connect('db.db')

cursor=connention.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employess(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL
)
''')
