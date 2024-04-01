from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from modules.models import *
from sqlalchemy import text

student = Blueprint("student", __name__)

def get_assignment_grades():
    cur_id = get_utorid_by_username(session['username'])
    sql = 'SELECT Assignment.aid, Assignment.name, Assignment_Grade.grade, Assignment.due_date\
        FROM Assignment_Grade JOIN Assignment ON Assignment_Grade.aid = Assignment.aid AND\
            Assignment_Grade.sid = "' + str(cur_id) + '"';
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()
    
def get_exam_grades():
    cur_id = get_utorid_by_username(session['username'])
    sql = 'SELECT Exam.eid, Exam.name, Exam_Grade.grade, Exam.date FROM Exam JOIN Exam_Grade\
        ON Exam_Grade.eid = Exam.eid AND Exam_Grade.sid = "' + str(cur_id) + '"';
    # TODO: Ask why we have to connect
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()

# What's the different if we put methods in /info or create a new route for POST/GET    
# TODO: Add blocker to unauthenticated user
@student.route('/info')
@student.route('/student_grades.html')
def info():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    assignment_grades = get_assignment_grades()
    exam_grades = get_exam_grades()
    return render_template('student_grades.html', assignment_grades = assignment_grades\
                           , exam_grades = exam_grades)

def get_utorid_by_username(username):
    return Login.query.filter(Login.username == username).first().utorid

@student.route('/remark_request', methods = ['GET', 'POST'])
def remark():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    req = request.json
    cur_utorid = get_utorid_by_username(session['username'])
    if request.method == 'POST' and req.get('document-type').lower() == 'assignment':
        data = Assignment_Regrade_Request(sid = cur_utorid,
                                          aid = req.get('id'),
                                          description = req.get('desc'),
                                          comment = '')
    else:
        data = Exam_Regrade_Request(sid = cur_utorid,
                                    eid = req.get('id'),
                                    description = req.get('desc'),
                                    comment = '')
    db.session.add(data)
    db.session.commit()
    return redirect(url_for('student.info'))

# TODO:
# Ask better way to turn this code better (hardcode on html side)
# Ask how the password is leaked

def get_assignment_remark_req():
    ass_req = Assignment_Regrade_Request.query.all()
    cur_utorid = get_utorid_by_username(session['username'])
    ret = []
    for item in ass_req:
        print(item.aid)
        dict = {'name': Assignment.query.filter(Assignment.aid == item.aid).first().name,
            'mark': Assignment_Grade.query.filter(Assignment_Grade.aid == item.aid and\
                                                  Assignment_Grade.sid == cur_utorid).first().grade,
            'comment': item.comment}
        ret.append(dict)
    return ret

def get_exam_remark_req():
    exam_req = Exam_Regrade_Request.query.all()
    cur_utorid = get_utorid_by_username(session['username'])
    ret = []
    for item in exam_req:
        dict = {'name': Exam.query.filter(Exam.eid == item.eid).first().name,
            'mark': Exam_Grade.query.filter(Exam_Grade.eid == item.eid and \
                                            Exam_Grade.sid == cur_utorid).first().grade,
            'comment': item.comment}
        ret.append(dict)
    return ret

@student.route('/my_remark_request')
@student.route('/student_remark.html')
def my_remark_request():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    return render_template('student_remark.html', 
                           assignment_remark_results = get_assignment_remark_req(),
                           exam_remark_results = get_exam_remark_req())