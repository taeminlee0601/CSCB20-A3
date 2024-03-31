from flask import flash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'Student'
    utorid = db.Column(db.String(20), primary_key = True)
    name = db.Column(db.String(100), nullable = False)

class Instructor(db.Model):
    __tablename__ = 'Instructor'
    utorid = db.Column(db.String(20), primary_key = True)
    name = db.Column(db.String(100), nullable = False)

class Assignment(db.Model):
    __tablename__ = 'Assignment'
    aid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(30), nullable = False)
    due_date = db.Column(db.String(20), nullable = False)
    description = db.Column(db.String(2000), nullable = False)
    weight = db.Column(db.Float, nullable = False)
    total_point = db.Column(db.Integer, nullable = False)

class Assignment_Grade(db.Model):
    __tablename__ = 'Assignment_Grade'
    sid = db.Column(db.String(20), primary_key = True)
    aid = db.Column(db.Integer)
    grade = db.Column(db.Float)

class Exam(db.Model):
    __tablename__ = 'Exam'
    eid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(30), nullable = False)
    date = db.Column(db.String(20), nullable = False)
    weight = db.Column(db.Float, nullable = False)

class Exam_Grade(db.Model):
    __tablename__ = 'Exam_Grade'
    sid = db.Column(db.String(20), primary_key = True)
    eid = db.Column(db.Integer)
    grade = db.Column(db.Float)

class Assignment_Regrade_Request(db.Model):
    __tablename__ = 'Assignment_Regrade_Request'
    reqid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    sid = db.Column(db.String(20)) 
    aid = db.Column(db.Integer)
    description = db.Column(db.String(2000))

class Exam_Regrade_Request(db.Model):
    __tablename__ = 'Exam_Regrade_Request'
    reqid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    sid = db.Column(db.String(20)) 
    eid = db.Column(db.Integer)
    description = db.Column(db.String(2000))

class Login(db.Model):
    __tablename__ = 'Login'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(20), unique=True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    user_type = db.Column(db.String(20), nullable = False)

class Feedback(db.Model):
    __tablename__ = 'Feedback'
    iid = db.Column(db.String(20), primary_key = True)
    like_about_instructor = db.Column(db.String(2000))
    improve_instructor = db.Column(db.String(2000))
    like_about_lab = db.Column(db.String(2000))
    improve_lab = db.Column(db.String(2000))

