from flask import Blueprint, render_template

student = Blueprint("student", __name__)

@student.route('/info')
def info():
    
    return render_template('student_grades.html')

@student.route('/my_remark_request')
def my_remark_request():

    return render_template('student_remark.html')