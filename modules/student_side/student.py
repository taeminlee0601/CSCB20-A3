from flask import Blueprint, render_template

student = Blueprint("student", __name__)

@student.route('/info')
def info():
    
    return render_template('student_grades.html')