from modules.models import *
from sqlalchemy import text

def get_all_assignment_info():
    '''
    Return all assignment information(aid, aname, due_date)
    '''
    sql = 'SELECT Assignment.aid, Assignment.name, Assignment.due_date FROM Assignment_Grade'
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()
    
def get_all_exam_info():
    '''
    Return all exam information(id, name, grade, date)
    '''
    sql = 'SELECT Exam.eid, Exam.name, Exam_Grade.grade, Exam.date FROM Exam'
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()