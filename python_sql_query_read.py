import sqlite3

connect = sqlite3.connect('python_sql.db')
connect.row_factory = sqlite3.Row
cursor = connect.cursor()


def read_data():
    """Function query and display data."""
    cursor.execute(
        """
        SELECT student.id,firstname,surname,classroom_id FROM student, classroom
        WHERE student.classroom_id=classroom.id
        """)

    schoolchild_read = cursor.fetchall()

    for student_read in schoolchild_read:
        print(student_read['id'],
              student_read['firstname'],
              student_read['surname'],
              student_read['classroom_id'], '\t')


read_data()
