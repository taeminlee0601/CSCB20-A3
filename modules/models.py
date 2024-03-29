from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class Student(db.Model):
    __tablename__ = 'Student'
    utorid = db.Column(db.String(10), primary_key = True)
    name = db.Column(db.String(100), nullable = False)

class Instructor(db.Model):
    __tablename__ = 'Instructor'
    utorid = db.Column(db.String(10), primary_key = True)
    name = db.Column(db.String(100), nullable = False)

class Login(db.Model):
    __tablename__ = 'Login'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(20), unique=True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    user_type = db.Column(db.String(20), nullable = False)


def add_person_to_db(login_info, student_info):
    if check_user_exist(login_info.username):
        flash('This username is already exist!')
        return
    # hash password before login
    login_info.password = bcrypt.generate_password_hash(login_info.password).decode('utf-8')
    db.session.add(login_info)
    db.session.add(student_info)
    db.session.commit()
    flash('Register user sucessfully!')

def get_login_info():
    return Login.query.all()

def check_user_exist(username):
    all_users = get_login_info()
    for user in all_users:
        if user.username == username:
            return True
    return False

def login_check(login_info):
    get_user = Login.query.filter_by(username = login_info[0]).first()
    if get_user == None:
        return False
    return get_user.username == login_info[0] and bcrypt.check_password_hash(get_user.password, login_info[1])