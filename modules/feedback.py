from flask import Blueprint, redirect, url_for, render_template, session, request
from modules.models import *
from modules.instructor import get_id_by_name
# Should i use one session or multiple session?

fb = Blueprint('feedback', __name__)

@fb.route('/feedback', methods = ['GET', 'POST'])
@fb.route('/feedback.html', methods = ['GET', 'POST'])
def feedback():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    if request.method == 'POST':
        fb_value = Feedback(iid = get_id_by_name(request.form['instructor']),
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

def display_feedback():
    # TODO
    pass

def add_feedback_to_db(fb_value):
    db.session.add(fb_value)
    db.session.commit()

def query_feedback():
    return Feedback.query.all()

