from flask import Flask, render_template, redirect, url_for, session, request
from datetime import timedelta
from modules.models import db, get_name_by_username
from modules.auth import auth, bcrypt
from modules.feedback import fb
from modules.student_side.student import student
from modules.instructor_side.instructor import ins


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b913f47618cb5c3d870b48d7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cscb20_a3.db'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=40)

db.init_app(app)
with app.app_context():
    db.create_all()
bcrypt.init_app(app)
app.register_blueprint(auth)
app.register_blueprint(fb)
app.register_blueprint(student)
app.register_blueprint(ins)

@app.route('/home')
@app.route('/index.html')
def home():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    pagename = 'Home'
    name = get_name_by_username(session['username']);
    return render_template('index.html', pagename=pagename, user_type = session['user-type'], name=name)

@app.route('/assignment.html')
@app.route('/assignment')
def assignment():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    
    pagename = 'Assignment'
    return render_template('assignment.html', pagename=pagename, user_type = session['user-type'])

@app.route('/calendar')
@app.route('/calendar.html')
def calendar():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    pagename = 'Calendar'
    return render_template('calendar.html', pagename=pagename, user_type = session['user-type'])

@app.route('/course_description')
@app.route('/course_description.html')
def course_description():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    pagename = 'Course Description'
    return render_template('course_description.html', pagename=pagename, user_type = session['user-type'])

@app.route('/course_team')
@app.route('/course_team.html')
def course_team():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    pagename = 'Course Team'
    return render_template('course_team.html', pagename=pagename, user_type = session['user-type'])

@app.route('/lectures')
@app.route('/lectures.html')
def lectures():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    pagename = 'Lectures'
    return render_template('lectures.html', pagename=pagename, user_type = session['user-type'])

@app.route('/resources')
@app.route('/resources.html')
def resources():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    pagename = 'Resources'
    return render_template('resources.html', pagename=pagename, user_type = session['user-type'])

@app.route('/syllabus')
@app.route('/syllabus.html')
def syllabus():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    pagename = 'Syllabus'
    return render_template('syllabus.html', pagename=pagename, user_type = session['user-type'])

@app.route('/tests')
@app.route('/tests.html')
def tests():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    pagename = 'Tests'
    return render_template('tests.html', pagename=pagename, user_type = session['user-type'])

@app.route('/tutorials')
@app.route('/tutorials.html')
def tutorials():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    pagename = 'Tutorials'
    return render_template('tutorials.html', pagename=pagename, user_type = session['user-type'])

@app.route('/logout', methods=['GET', 'POST'])
def log_out():
    # return render_template('lectures.html', pagename='Sign in')
    session.clear()
    return redirect(url_for('auth.signin'))

if __name__=="__main__":
    app.run(debug=True)