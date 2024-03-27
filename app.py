from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'b913f47618cb5c3d870b48d7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cscb20_a3.db'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'Student'
    utorid = db.Column(db.String(10), primary_key = True)
    name = db.Column(db.String(100), nullable = False)

class Login(db.Model):
    __tablename__ = 'Login'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(20), unique=True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    user_type = db.Column(db.String(20), nullable = False)


@app.route('/')
@app.route('/home')
@app.route('/index.html')
def home():
    pagename = 'Home'
    return render_template('index.html', pagename=pagename)

@app.route('/assignment.html')
@app.route('/assignment')
def assignment():
    pagename = 'Assignment'
    return render_template('assignment.html', pagename=pagename)

@app.route('/calendar')
@app.route('/calendar.html')
def calendar():
    pagename = 'Calendar'
    return render_template('calendar.html', pagename=pagename)

@app.route('/course_description')
@app.route('/course_description.html')
def course_description():
    pagename = 'Course Description'
    return render_template('course_description.html', pagename=pagename)

@app.route('/course_team')
@app.route('/course_team.html')
def course_team():
    pagename = 'Course Team'
    return render_template('course_team.html', pagename=pagename)

@app.route('/feedback')
@app.route('/feedback.html')
def feedback():
    pagename = 'Feedback'
    return render_template('feedback.html', pagename=pagename)

@app.route('/lectures')
@app.route('/lectures.html')
def lectures():
    pagename = 'Lectures'
    return render_template('lectures.html', pagename=pagename)

@app.route('/resources')
@app.route('/resources.html')
def resources():
    pagename = 'Resources'
    return render_template('resources.html', pagename=pagename)

@app.route('/syllabus')
@app.route('/syllabus.html')
def syllabus():
    pagename = 'Syllabus'
    return render_template('syllabus.html', pagename=pagename)

@app.route('/tests')
@app.route('/tests.html')
def tests():
    pagename = 'Tests'
    return render_template('tests.html', pagename=pagename)

@app.route('/tutorials')
@app.route('/tutorials.html')
def tutorials():
    pagename = 'Tutorials'
    return render_template('tutorials.html', pagename=pagename)

@app.route('/signin', methods = ['GET', 'POST'])
@app.route('/signin.html', methods = ['GET', 'POST'])
def signin():
    pagename = 'Sign in'
    return render_template('signin.html', pagename=pagename)

@app.route('/signup', methods = ['GET', 'POST'])
@app.route('/signup.html', methods = ['GET', 'POST'])
def signup():
    pagename = 'Sign up'
    if request.method == 'POST':
        hash_pw = bcrypt.generate_password_hash(request.form['input-password']).decode('utf-8')
        info = (request.form['user-type'],
                request.form['input-full-name'], 
                request.form['input-utorid'],
                request.form['input-username'], 
                hash_pw)
        add_person_to_db(info)
    return render_template('signup.html', pagename=pagename)

def get_login_info():
    return Login.query.all()

def check_user_exist(username):
    all_users = get_login_info()
    for user in all_users:
        if user.username == username:
            return True
    return False

def add_person_to_db(info):
    # TODO: check if user exist
    if check_user_exist(info[3]):
        flash('User is already exist!')
        return
    # add info to Login
    login_info = Login(username = info[3], password = info[4], user_type = info[0])
    db.session.add(login_info)

    # add information to Student
    student_info = Student(utorid = info[2], name = info[1])
    db.session.add(student_info)

    db.session.commit()

if __name__=="__main__":
    app.run(debug=True)