import os
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


if os.path.exists('sqlalchemy.db'):
    os.remove('sqlalchemy.db')

# create instance class Engine to service database
database = create_engine('sqlite:///sqlalchemy.db')

# class base
SQLAlchemyModel = declarative_base()


# class Classroom and Student describe records tables and relationship among them
class Classroom(SQLAlchemyModel):
    __tablename__ = 'classroom'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    profile = Column(String(20), default='')
    school_pupils = relationship('Student', backref='classroom')


class Student(SQLAlchemyModel):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=False)
    classroom_id = Column(Integer, ForeignKey('classroom.id'))


# create tables
SQLAlchemyModel.metadata.create_all(database)


# create session thant stores objects and allows talk to database
DatabaseSession = sessionmaker(bind=database)
session = DatabaseSession()

# add two classes, if table is empty
if not session.query(Classroom).count():
    session.add(Classroom(name='1A', profile='programing'))
    session.add(Classroom(name='1B', profile='web'))


# create instance Classroom represent "1A"
instance_classroom_1a = session.query(Classroom).filter_by(name='1A').one()

# added data many students
session.add_all([
    Student(firstname='Jan', surname='Kowalski', classroom_id=instance_classroom_1a.id),
    Student(firstname='Janusz', surname='Nowak', classroom_id=instance_classroom_1a.id),
    Student(firstname='Janek', surname='Nowacki', classroom_id=instance_classroom_1a.id)
])


def read_data():
    for student in session.query(Student).join(Classroom).all():
        print(student.id,
              student.firstname,
              student.surname,
              student.classroom_id)


# change classroom student with id 2
instance_student = session.query(Student).filter(Student.id == 2).one()
instance_student.classroom_id = session.query(Classroom.id).filter(Classroom.name == '1B').scalar()

read_data()

# delete student with id 3
session.delete(session.query(Student).get(3))

# save changes and close session
session.commi()
session.close()
