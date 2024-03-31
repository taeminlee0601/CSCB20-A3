from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for, session
from modules.models import *
from flask_bcrypt import Bcrypt

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth.route('/', methods = ['GET', 'POST'])
@auth.route('/signin', methods = ['GET', 'POST'])
@auth.route('/signin.html', methods = ['GET', 'POST'])
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

@auth.route('/signup', methods = ['GET', 'POST'])
@auth.route('/signup.html', methods = ['GET', 'POST'])
def signup():
    pagename = 'Sign up'
    if request.method == 'POST':
        login_info = Login(username = request.form['input-username'],
                           password = request.form['input-password'],
                           user_type = request.form['user-type'],
                           utorid = request.form['input-utorid'],
                           name = request.form['input-full-name'])
        add_person_to_db(login_info)
    return render_template('signup.html', pagename=pagename)

def add_person_to_db(login_info):
    if check_user_exist(login_info.username):
        flash('This username is already exist!')
        return
    # hash password before login
    login_info.password = bcrypt.generate_password_hash(login_info.password).decode('utf-8')
    db.session.add(login_info)
    db.session.commit()
    flash('Register user sucessfully!')

def get_login_info():
    return Login.query.all()

def check_user_exist(username):
    all_users = get_login_info()
    for user in all_users:
        if user.username == username:
            return True
    return False

def login_check(login_info):
    get_user = Login.query.filter_by(username = login_info[0]).first()
    if get_user == None:
        return False
    return get_user.username == login_info[0] and bcrypt.check_password_hash(get_user.password, login_info[1])