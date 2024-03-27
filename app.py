from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import timedelta

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'b913f47618cb5c3d870b48d7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cscb20_a3.db'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=40)

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'Student'
    utorid = db.Column(db.String(10), primary_key = True)
    name = db.Column(db.String(100), nullable = False)

class Instructor(db.Model):
    __tablename__ = 'Instructor'
    utorid = db.Column(db.String(10), primary_key = True)
    name = db.Column(db.String(100), nullable = False)

class Login(db.Model):
    __tablename__ = 'Login'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(20), unique=True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    user_type = db.Column(db.String(20), nullable = False)


@app.route('/home')
@app.route('/index.html')
def home():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Home'
    return render_template('index.html', pagename=pagename)

@app.route('/assignment.html')
@app.route('/assignment')
def assignment():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    
    pagename = 'Assignment'
    return render_template('assignment.html', pagename=pagename)

@app.route('/calendar')
@app.route('/calendar.html')
def calendar():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Calendar'
    return render_template('calendar.html', pagename=pagename)

@app.route('/course_description')
@app.route('/course_description.html')
def course_description():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Course Description'
    return render_template('course_description.html', pagename=pagename)

@app.route('/course_team')
@app.route('/course_team.html')
def course_team():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Course Team'
    return render_template('course_team.html', pagename=pagename)

@app.route('/feedback')
@app.route('/feedback.html')
def feedback():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Feedback'
    return render_template('feedback.html', pagename=pagename)

@app.route('/lectures')
@app.route('/lectures.html')
def lectures():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Lectures'
    return render_template('lectures.html', pagename=pagename)

@app.route('/resources')
@app.route('/resources.html')
def resources():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Resources'
    return render_template('resources.html', pagename=pagename)

@app.route('/syllabus')
@app.route('/syllabus.html')
def syllabus():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Syllabus'
    return render_template('syllabus.html', pagename=pagename)

@app.route('/tests')
@app.route('/tests.html')
def tests():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Tests'
    return render_template('tests.html', pagename=pagename)

@app.route('/tutorials')
@app.route('/tutorials.html')
def tutorials():
    if 'username' not in session.keys():
        return redirect(url_for('signin'))
    pagename = 'Tutorials'
    return render_template('tutorials.html', pagename=pagename)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/signin', methods = ['GET', 'POST'])
@app.route('/signin.html', methods = ['GET', 'POST'])
def signin():
    if 'username' in session.keys():
        return redirect(url_for('home'))
    
    pagename = 'Sign in'
    if request.method == 'POST':
        login_info = (request.form['input-username'],
                      request.form['input-password'])
        
        if login_check(login_info):
            session['username'] = login_info[0]
            session.permanent = True
            return redirect(url_for('home'))
        else:
            flash('Invalid username/password!')
    return render_template('signin.html', pagename=pagename)

def login_check(login_info):
    get_user = Login.query.filter_by(username = login_info[0]).first()
    if get_user == None:
        return False
    return get_user.username == login_info[0] and bcrypt.check_password_hash(get_user.password, login_info[1])

@app.route('/signup', methods = ['GET', 'POST'])
@app.route('/signup.html', methods = ['GET', 'POST'])
def signup():
    pagename = 'Sign up'
    if request.method == 'POST':
        hash_pw = bcrypt.generate_password_hash(request.form['input-password']).decode('utf-8')
        login_info = Login(username = request.form['input-username'],
                           password = hash_pw,
                           user_type = request.form['user-type'])
        user_info = None
        if login_info.user_type == 'instructor':
            user_info = Instructor(utorid = request.form['input-utorid'],
                                   name = request.form['input-full-name'])
        else:
            user_info = Student(utorid = request.form['input-utorid'],
                                   name = request.form['input-full-name'])
        add_person_to_db(login_info, user_info)
    return render_template('signup.html', pagename=pagename)

def get_login_info():
    return Login.query.all()

def check_user_exist(username):
    all_users = get_login_info()
    for user in all_users:
        if user.username == username:
            return True
    return False

def add_person_to_db(login_info, student_info):
    if check_user_exist(login_info.username):
        flash('This username is already exist!')
        return
    db.session.add(login_info)
    db.session.add(student_info)
    db.session.commit()
    flash('Register user sucessfully!')

if __name__=="__main__":
    app.run(debug=True)