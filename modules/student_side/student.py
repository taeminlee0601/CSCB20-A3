from flask import Blueprint, render_template, request, jsonify, session
from modules.models import *
from sqlalchemy import text

student = Blueprint("student", __name__)

def get_assignment_grades():
    sql = 'SELECT Assignment.name, Assignment_Grade.grade, Assignment.due_date\
        FROM Assignment_Grade JOIN Assignment ON Assignment_Grade.aid = Assignment.aid'
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()
    
def get_exam_grades():
    sql = 'SELECT Exam.name, Exam_Grade.grade, Exam.date FROM Exam JOIN Exam_Grade\
        ON Exam_Grade.eid = Exam.eid'
    # TODO: Ask why we have to connect
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()

# What's the different if we put methods in /info or create a new route for POST/GET    
@student.route('/info')
def info():
    assignment_grades = get_assignment_grades()
    exam_grades = get_exam_grades()
    return render_template('student_grades.html', assignment_grades = assignment_grades\
                           , exam_grades = exam_grades)

def get_utorid_by_username(username):
    return Login.query.filter(Login.username == username).first().utorid

@student.route('/remark_request', methods = ['GET', 'POST'])
def remark():
    req = request.json
    if req.get('document-type').lower() == 'assignment':
        cur_utorid = get_utorid_by_username(session['username'])
        data = Assignment_Regrade_Request(sid = cur_utorid,
                                          aid = req.get(''))
    pass
# TODO:
# Ask better way to turn this code better (hardcode on html side)
# Ask how the password is leaked

@student.route('/my_remark_request')
@student.route('/student_remark.html')
def my_remark_request():
    return render_template('student_remark.html')