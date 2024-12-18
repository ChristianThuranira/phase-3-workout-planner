from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    workouts = relationship('Workout', back_populates='user')

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    exercises = relationship('Exercise', back_populates='workout')
    user = relationship('User', back_populates='workouts')

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    repetitions = Column(Integer)
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    workout = relationship('Workout', back_populates='exercises')
