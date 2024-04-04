from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from modules.models import *
from sqlalchemy import text

def get_assignment_grades():
    '''
    Return assignment information(aid, name, grade, due_date) of a current student 
    in session['username'] 
    '''
    cur_id = get_utorid_by_username(session['username'])
    sql = 'SELECT Assignment.aid, Assignment.name, Assignment_Grade.grade, Assignment.due_date\
        FROM Assignment_Grade JOIN Assignment ON Assignment_Grade.aid = Assignment.aid AND\
            Assignment_Grade.sid = "' + str(cur_id) + '"';
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()
    
def get_all_assignment_grades(aid):
    '''
    Return assignment information(sid, name, grade) of a given assignment id 'aid'
    '''
    return Assignment_Grade.query.filter(Assignment_Grade.aid == aid).all()

def get_all_exam_grades(eid):
    '''
    Return assignment information(sid, name, grade) of a given exam id 'eid'
    '''
    return Exam_Grade.query.filter(Exam_Grade.eid == eid).all()
    
def get_exam_grades():
    '''
    Return exam information(eid, name, grade, date) of a current student in 
    session['username'] 
    '''
    cur_id = get_utorid_by_username(session['username'])
    sql = 'SELECT Exam.eid, Exam.name, Exam_Grade.grade, Exam.date FROM Exam JOIN Exam_Grade\
        ON Exam_Grade.eid = Exam.eid AND Exam_Grade.sid = "' + str(cur_id) + '"';
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()
    
def update_grades(new_grade_info):
    '''
    Update grade to the database on given the dictionary 'new_grade_info' including
    (sid, aid, (new) grade)
    '''
    if new_grade_info['aid'][0] == 'a': # assignment type
        sql = 'UPDATE Assignment_Grade SET Assignment_Grade.grade = ' + new_grade_info['grade']\
              + ' WHERE Assignment_Grade.aid == "' + new_grade_info['aid'] + '"\
                AND Assignment_Grade.sid == "' + new_grade_info['sid']
        with db.engine.connect() as conn:
            conn.execute(sql)
    elif new_grade_info['aid'][1] == 'e': # exam type
        sql = 'UPDATE Exam_Grade SET Exam_Grade.grade = ' + new_grade_info['grade']\
              + ' WHERE Exam_Grade.eid == "' + new_grade_info['eid'] + '"\
                AND Exam_Grade.sid == "' + new_grade_info['sid']
        with db.engine.connect() as conn:
            conn.execute(sql)
