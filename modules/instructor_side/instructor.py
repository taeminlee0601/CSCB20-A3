from modules.models import *
from flask import Blueprint, session, render_template, redirect, url_for, request
from modules.feedback import get_feedback
from modules.models import *
from modules.student_side.assessment_info import *
from modules.student_side.grades import *
from modules.student_side.remark_req import *

ins = Blueprint('instructor', __name__)
stu_grade_info = []

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

def update_student_info(assessment_id):
    '''
    Update all grades and all students information (sid, aid, grade) to global list
    'stu_grade_info' base on a given assessment id 'assessment_id'
    '''
    stu_grade_info.clear()
    # assignment type
    if assessment_id[0] == 'a':
        res = get_all_assignment_grades(assessment_id)
        for item in res:
            stu_grade_info.append((item.sid, item.aid, item.grade))
    # exam type
    elif assessment_id[0] == 'e':
        res = get_all_exam_grades(assessment_id)
        for item in res:
            stu_grade_info.append((item.sid, item.eid, item.grade))
    print(stu_grade_info)

@ins.route('/manage_grades', methods = ['GET', 'POST'])
@ins.route('/instructor_grades.html', methods = ['GET', 'POST'])
def manage_grades():
    if session['user-type'] != 'instructor':
        return redirect(url_for('home'))
    if request.method == 'POST':
        assessment_id = request.json # request send type of assesment
        update_student_info(assessment_id['data'])
        return redirect(url_for('instructor.edit_student_grades'))
    return render_template('instructor_grades.html', ass_info = get_all_assignment_info()\
                           , exam_info = get_all_exam_info())

@ins.route('/edit_grades', methods = ['GET', 'POST'])
def edit_student_grades():
    # This function will return render_template two times
    # First one is from redirect(url_for) from POST request, and have to return back to the response
    # --> can not load the webpage properly
    # Since stu_grade_info is global variable so we can make a GET request again
    # to load the page properly and pass stu_grade_info
    if request.method == 'POST':
        # update mark into database
        new_grade_info = request.json
        print(new_grade_info) # Added to check if data is passed correctly
        update_grades(new_grade_info)
        return redirect(url_for('instructor.edit_student_grades'))

    assessment_name = ''
    if len(stu_grade_info) > 0:
        if stu_grade_info[0][1][0] == 'e': # exam type
            assessment_name = get_exam_name_by_eid(stu_grade_info[0][1])
        if stu_grade_info[0][1][0] == 'a': # assignment type
            assessment_name = get_assignment_name_by_id(stu_grade_info[0][1])
        update_student_info(stu_grade_info[0][1])
    
    return render_template('edit_student_grades.html', stu_grade_info = stu_grade_info, \
    assessment_name = assessment_name)

@ins.route('/manage_remark_request', methods = ['GET', 'POST'])
@ins.route('/instructor_remarks.html', methods = ['GET', 'POST'])
def manage_remark_request():
    if request.method == 'POST':
        # update mark and comment to database
        pass
    ret_ass_req = get_assignment_remark_req()
    ret_exam_req = get_exam_remark_req()
    exam_reqs = []
    ass_reqs = []
    for item in ret_ass_req:
        ass_reqs.append((item.reqid, item.sid, item.aid, item.description))
    for item in ret_exam_req:
        exam_reqs.append((item.reqid, item.sid, item.aid, item.description))
    return render_template('instructor_remarks.html', exam_reqs = exam_reqs, \
                           ass_reqs = ass_reqs)