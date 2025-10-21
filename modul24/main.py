import sqlite3

connention= sqlite3.connect('db.db')

cursor=connention.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employess(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL
)
''')



connention.commit()


cursor.execute('''
    INSERT INTO employess(name,position,department,salary)
    VALUES (?,?,?,?)'''
               ,('John Doe','SWD' , 'IT', 70000))
               
               
connention.commit()

cursor.execute("SELECT * FROM employess")


rows=cursor.fetchall()
for row in rows:
    print(f"employess : {rows[0]},workPlace: {row[1]}")