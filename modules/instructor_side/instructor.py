from modules.models import *
from flask import Blueprint, session, render_template, redirect, url_for, request
from modules.feedback import get_feedback
from modules.models import *
from modules.student_side.assessment_info import *

ins = Blueprint('instructor', __name__)

# - Display feedback from students (anonymously)
# - Add/Edit/Remove student's mark
# - Show regrade request from a particular student and assignment/exam 

@ins.route('/view_my_feedback')
@ins.route('/instructor_feedbacks.html')
def display_feedback():
    '''
    Get the feedback to the database and display it on the website
    '''
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    if session['user-type'] != 'instructor':
        return redirect(url_for('home'))
    feedback_all = get_feedback()
    rsp_q1 = []
    rsp_q2 = []
    rsp_q3 = []
    rsp_q4 = []
    for item in feedback_all:
        if item.like_about_instructor != '':
            rsp_q1.append(item.like_about_instructor)
        if item.improve_instructor != '':
            rsp_q2.append(item.improve_instructor)
        if item.like_about_lab != '':
            rsp_q3.append(item.like_about_lab)
        if item.improve_lab != '':
            rsp_q4.append(item.improve_lab)
    # print(rsp_q1, rsp_q2, rsp_q3, rsp_q4)
    return render_template('feedback.html', rsp_q1 = rsp_q1, rsp_q2 = rsp_q2, \
                           rsp_q3 = rsp_q3, rsp_q4 = rsp_q4)

# def edit_student_grade():
#     pass

# def remove_student_grade():
#     pass

# @ins.route('/add_grades', method=['GET', 'POST'])
# def add_student_grade():
#     '''
#     Receive the grades from the request and sent it to database
#     '''    
#     if request.method == 'POST':
#         sid = get_utorid_by_username(request.form['input-student-name'])
#         aid = get_assignment_id_by_name(request.form['input-assessment-name'])
#         mark = request.form['input-mark']
#     return None

@ins.route('/manage_grades')
@ins.route('/instructor_grades.html')
def manage_grades():
    if session['user-type'] != 'instructor':
        return redirect(url_for('home'))
    return render_template('instructor_grades.html', ass_info = get_all_assignment_info()\
                           , exam_info = get_all_exam_info())

@ins.route('/edit_grades', methods = ['GET', 'POST'])
@ins.route('/edit_student_grades.html', methods = ['GET', 'POST'])
def edit_student_grades():
    if request.method == 'POST':
        assessment_type = request.json
        # TODO: change assessment_type['attributes']
        if assessment_type['type'] == 'exam':
            pass
        elif assessment_type['type'] == 'assignment':
            pass
