import os
from peewee import *


if os.path.exists('python_orm_peewee.db'):
    os.remove('python_orm_peewee.db')


data = SqliteDatabase('python_orm_peewee.db')  # :memory: RAM


class PeeweeModel(Model):
    class Meta:
        database = data


class Classroom(PeeweeModel):
    name = CharField(null=False)
    profile = CharField(default='')


class Student(PeeweeModel):
    firstname = CharField(null=False)
    surname = CharField(null=False)
    classroom_id = ForeignKeyField(Classroom, related_name='schoolchild')


data.connect()  # connect with database
data.create_tables([Classroom, Student])  # create table


# add two class, when table is empty
if Classroom().select().count() == 0:
    instance_classroom = Classroom(name='1A', profile='developer')
    instance_classroom.save()
    instance_classroom = Classroom(name='1B', profile='programing')
    instance_classroom.save()

# select id classroom
select_id_classroom = Classroom.select().where(Classroom.name == '1A').get()

# list student
list_schoolchild = [
    {'firstname': 'Jan', 'surname': 'Nowak', 'classroom_id': select_id_classroom},
    {'firstname': 'Janek', 'surname': 'Kowalski', 'classroom_id': select_id_classroom},
    {'firstname': 'Janusz', 'surname': 'Nowacki', 'classroom_id': select_id_classroom}
]

# add many student in one instruction
Student.insert_many(list_schoolchild).execute()


def read_data():
    for student_read in Student.select().join(Classroom):
        print(student_read.id,
              student_read.firstname,
              student_read.surname,
              student_read.classroom_id)


# read_data()


# change student's classroom
student_change_classroom = Student().select().join(Classroom).where(Student.id == 2).get()
student_change_classroom.classroom = Classroom.select().where(Classroom.name == '1B').get()
student_change_classroom.save()


# delete student
Student.select().where(Student.id == 3).get().delete_instance()

read_data()

data.close()
