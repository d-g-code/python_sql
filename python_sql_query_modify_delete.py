import sqlite3
import python_sql_query_read


connect = sqlite3.connect('python_sql.db')
connect.row_factory = sqlite3.Row
cursor = connect.cursor()

#  change classroom student with identity 2
cursor.execute('SELECT id FROM classroom WHERE name = ?', ('1B',))
new_classroom_id = cursor.fetchone()[0]
cursor.execute('UPDATE student SET classroom_id = ? WHERE id = ?', (new_classroom_id, 2))

#  delete student with identity 3
cursor.execute('DELETE FROM student WHERE id = ?', (3,))
