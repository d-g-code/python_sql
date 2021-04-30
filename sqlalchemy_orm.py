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


