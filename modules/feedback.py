from flask import Blueprint, redirect, url_for, render_template, session, request
from sqlalchemy import text
from modules.models import *

fb = Blueprint('feedback', __name__)

@fb.route('/feedback', methods = ['GET', 'POST'])
@fb.route('/feedback.html', methods = ['GET', 'POST'])
def feedback():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    if request.method == 'POST':
        fb_value = Feedback(iid = get_instructor_id_by_name(request.form['instructor']),
                            like_about_instructor = request.form['qs-like-about-instructor'],
                            improve_instructor = request.form['qs-improve-instructor'],
                            like_about_lab = request.form['qs-like-about-lab'],
                            improve_lab = request.form['qs-improve-lab'])
        if fb_value.iid == -1:
            # TODO: add this msg to front-end
            flash('This instructor does not exist')
        else:
            add_feedback_to_db(fb_value)

    pagename = 'Feedback'
    return render_template('feedback.html', pagename=pagename)

def get_feedback():
    '''
    Returns all feedback for current instructor, if the user is not an instructor
    then 
    '''
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    
    sql = 'select like_about_instructor, improve_instructor, like_about_lab, \
        improve_lab from feedback where iid = "' + str(session['username']) + '"'
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()

def add_feedback_to_db(fb_value):
    '''
    Add feedback 'fb_value' into current database
    '''
    db.session.add(fb_value)
    db.session.commit()

def query_feedback():
    '''
    Return all feedback from the students in Feedback schema
    '''
    return Feedback.query.all()

