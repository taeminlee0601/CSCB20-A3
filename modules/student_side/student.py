from flask import Blueprint, render_template, request, session, redirect, url_for
from modules.models import *
from modules.student_side.remark_req import *
from modules.student_side.grades import *

student = Blueprint("student", __name__)

@student.route('/info')
@student.route('/student_grades.html')
def info():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    assignment_grades = get_assignment_grades()
    exam_grades = get_exam_grades()
    return render_template('student_grades.html', assignment_grades = assignment_grades\
                           , exam_grades = exam_grades)

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

@student.route('/my_remark_request')
@student.route('/student_remark.html')
def my_remark_request():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    return render_template('student_remark.html', 
                           assignment_remark_results = get_assignment_remark_req(),
                           exam_remark_results = get_exam_remark_req())