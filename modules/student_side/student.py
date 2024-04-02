from flask import Blueprint, render_template

student = Blueprint("student", __name__)

@student.route('/info')
@student.route('/student_grades.html')
def info():
    pagename = 'info'
    return render_template('student_grades.html', pagename=pagename)

@student.route('/my_remark_request')
@student.route('/student_remark.html')
def my_remark_request():
    pagename = 'my_remark_request'
    return render_template('student_remark.html', pagename=pagename)