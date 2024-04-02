from modules.models import *
from flask import Blueprint, session, render_template, redirect, url_for, request
from modules.feedback import get_feedback
from modules.models import *

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
    return render_template('feedback.html', feedback_all = get_feedback())

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
    return render_template('instructor_grades.html')