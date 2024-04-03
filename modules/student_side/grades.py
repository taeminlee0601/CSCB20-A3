from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from modules.models import *
from sqlalchemy import text

def get_assignment_grades():
    '''
    Return assignment information(id, name, grade, due_date) of a current student 
    in session['username'] 
    '''
    cur_id = get_utorid_by_username(session['username'])
    sql = 'SELECT Assignment.aid, Assignment.name, Assignment_Grade.grade, Assignment.due_date\
        FROM Assignment_Grade JOIN Assignment ON Assignment_Grade.aid = Assignment.aid AND\
            Assignment_Grade.sid = "' + str(cur_id) + '"';
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()
    
def get_exam_grades():
    '''
    Return exam information(id, name, grade, date) of a current student in 
    session['username'] 
    '''
    cur_id = get_utorid_by_username(session['username'])
    sql = 'SELECT Exam.eid, Exam.name, Exam_Grade.grade, Exam.date FROM Exam JOIN Exam_Grade\
        ON Exam_Grade.eid = Exam.eid AND Exam_Grade.sid = "' + str(cur_id) + '"';
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()
