from flask import Blueprint, redirect, url_for, render_template, session, request, flash
from modules.models import *
from modules.instructor_side.instructor import get_list_of_instructor

fb = Blueprint('feedback', __name__)


def add_feedback_to_db(fb_value):
    '''
    Add feedback 'fb_value' into current database
    '''
    db.session.add(fb_value)
    db.session.commit()

@fb.route('/feedback', methods = ['GET', 'POST'])
@fb.route('/feedback.html', methods = ['GET', 'POST'])
def feedback():
    if 'username' not in session.keys():
        return redirect(url_for('auth.signin'))
    if request.method == 'POST':
        fb_value = Feedback(iid = request.form['instructor'],
                            like_about_instructor = request.form['qs-like-about-instructor'],
                            improve_instructor = request.form['qs-improve-instructor'],
                            like_about_lab = request.form['qs-like-about-lab'],
                            improve_lab = request.form['qs-improve-lab'])
        print(request.form['instructor'])
        if fb_value.iid == -1:
            # TODO: add this msg to front-end
            flash('This instructor does not exist')
        else:
            add_feedback_to_db(fb_value)

    pagename = 'Feedback'
    return render_template('feedback.html', pagename=pagename, instructors = get_list_of_instructor())