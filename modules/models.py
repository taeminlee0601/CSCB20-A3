from flask import flash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Assignment(db.Model):
    __tablename__ = 'Assignment'
    aid = db.Column(db.String(5), primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    due_date = db.Column(db.String(20), nullable = False)
    description = db.Column(db.String(2000), nullable = False)
    weight = db.Column(db.Float, nullable = False)
    total_point = db.Column(db.Integer, nullable = False)
    assignment_grades = db.relationship('Assignment_Grade', backref='assignments', lazy = True)

class Assignment_Grade(db.Model):
    __tablename__ = 'Assignment_Grade'
    sid = db.Column(db.String(20), primary_key = True)
    aid = db.Column(db.String(5), db.ForeignKey('Assignment.aid'), primary_key = True, nullable = False)
    grade = db.Column(db.Float, nullable = False)

class Exam(db.Model):
    __tablename__ = 'Exam'
    eid = db.Column(db.String(5), primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    date = db.Column(db.String(20), nullable = False)
    weight = db.Column(db.Float, nullable = False)
    exam_grades = db.relationship('Exam_Grade', backref='exams', lazy=True)

class Exam_Grade(db.Model):
    __tablename__ = 'Exam_Grade'
    sid = db.Column(db.String(20), primary_key = True)  
    eid = db.Column(db.String(5), db.ForeignKey('Exam.eid'), primary_key = True)
    grade = db.Column(db.Float)

class Assignment_Regrade_Request(db.Model):
    __tablename__ = 'Assignment_Regrade_Request'
    reqid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    sid = db.Column(db.String(20)) 
    aid = db.Column(db.String(5))
    description = db.Column(db.String(2000))
    comment = db.Column(db.String(2000))

class Exam_Regrade_Request(db.Model):
    __tablename__ = 'Exam_Regrade_Request'
    reqid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    sid = db.Column(db.String(20)) 
    eid = db.Column(db.String(5))
    description = db.Column(db.String(2000))
    comment = db.Column(db.String(2000))

class Login(db.Model):
    __tablename__ = 'Login'
    utorid = db.Column(db.String(20), primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    username = db.Column(db.String(20), unique=True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    user_type = db.Column(db.String(20), nullable = False)

class Feedback(db.Model):
    __tablename__ = 'Feedback'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    iid = db.Column(db.String(20))
    like_about_instructor = db.Column(db.String(2000))
    improve_instructor = db.Column(db.String(2000))
    like_about_lab = db.Column(db.String(2000))
    improve_lab = db.Column(db.String(2000))

def get_utorid_by_username(username):
    '''
    Return utorid by given 'username'
    '''
    return Login.query.filter(Login.username == username).first().utorid

def get_instructor_id_by_name(name):
    '''
    Return instructor utorid by instructor's name
    '''
    for instructor in Login.query.filter(Login.user_type == 'instructor').all():
        if name in instructor.name.lower():
            return instructor.utorid
    return -1

def get_assignment_id_by_name(assignment_name):
    '''
    Return assignment id based on name of the 'assignment_name'
    '''
    return Assignment.query.filter(Assignment.name == assignment_name).first().aid

def get_usertype_by_username(username):
    '''
    Return the user_type (either 'instructor' or 'student' by the username)
    '''
    return Login.query.filter(Login.username == username).first().user_type
