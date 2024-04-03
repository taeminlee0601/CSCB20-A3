from modules.models import *
from flask import Blueprint, session, render_template, redirect, url_for, request
from modules.feedback import get_feedback
from modules.models import *
from modules.student_side.assessment_info import *
from modules.student_side.grades import *

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

stu_grade_info = []
@ins.route('/manage_grades', methods = ['GET', 'POST'])
@ins.route('/instructor_grades.html', methods = ['GET', 'POST'])
def manage_grades():
    if session['user-type'] != 'instructor':
        return redirect(url_for('home'))
    if request.method == 'POST':
        assessment_id = request.json
        if assessment_id['data'][0] == 'a':
            res = get_all_assignment_grades(assessment_id['data'])
            for item in res:
                stu_grade_info.append((item.sid, item.aid, item.grade))
        elif assessment_id['data'][0] == 'e':
            res = get_all_exam_info(assessment_id['data'])
            for item in res:
                stu_grade_info.append((item.sid, item.sid, item.grade))
        return redirect(url_for('instructor.edit_student_grades'))
    return render_template('instructor_grades.html', ass_info = get_all_assignment_info()\
                           , exam_info = get_all_exam_info())

@ins.route('/edit_grades')
@ins.route('/edit_student_grades.html')
def edit_student_grades():
    # This function will return render_template two times
    # First one is from redirect(url_for) from POST request, and have to return back to the response
    # --> can not load the webpage properly
    # Since stu_grade_info is global variable so we can make a GET request again
    # to load the page properly and pass stu_grade_info
    return render_template('edit_student_grades.html', stu_grade_info = stu_grade_info)
