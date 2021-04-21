import sqlite3


connect = sqlite3.connect('python_sql.db')  # create connection to database stored on disk

connect.row_factory = sqlite3.Row  # access columns via index and via names

cursor = connect.cursor()  # create cursor object

cursor.execute("DROP TABLE IF EXISTS classroom")  # create table

#  individual statement use method 'execute'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS classroom (
        id INTEGER PRIMARY KEY ASC,
        name varchar(50) NOT NULL,
        profile varchar(50) DEFAULT ''
    )""")

#  many instruction use method 'executescript'
cursor.executescript("""
    DROP TABLE IF EXISTS student;
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY ASC,
        firstname varchar(50) NOT NULL,
        surname varchar(50) NOT NULL,
        classroom_id INTEGER NOT NULL,
        FOREIGN KEY(classroom_id) REFERENCES classroom(id)
    )""")

#  inserting one record
cursor.execute('INSERT INTO classroom VALUES(NULL, ?, ?);', ('1A', 'developer'))
cursor.execute('INSERT INTO classroom VALUES(NULL, ?, ?);', ('1B', 'hacker'))
cursor.execute('INSERT INTO classroom VALUES(NULL, ?, ?);', ('1C', 'web'))

#  execute query retrieve the id of classroom 1A from table classroom
cursor.execute('SELECT id FROM classroom WHERE name = ?', ('1A',))
classroom_id = cursor.fetchone()[0]

#  tuple with schoolchild
schoolchild = (
    (None, 'Jan', 'Kowalski', classroom_id),
    (None, 'Janek', 'Nowak', classroom_id),
    (None, 'Janusz', 'Kowalewski', classroom_id)
)

#  insert multiple records
cursor.executemany('INSERT INTO student VALUES(?,?,?,?)', schoolchild)

#  approve changes in database
connect.commit()
