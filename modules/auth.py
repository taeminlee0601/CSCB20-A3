from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for, session
from modules.models import *

auth = Blueprint('auth', __name__)

@auth.route('/', methods = ['GET', 'POST'])
@auth.route('/signin', methods = ['GET', 'POST'])
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