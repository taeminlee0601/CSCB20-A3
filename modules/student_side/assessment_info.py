from modules.models import *
from sqlalchemy import text

def get_all_assignment_info():
    '''
    Return all assignment information(aid, aname, due_date)
    '''
    sql = 'SELECT Assignment.aid, Assignment.name, Assignment.due_date FROM Assignment'
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()
    
def get_all_exam_info():
    '''
    Return all exam information(id, ename, date)
    '''
    sql = 'SELECT Exam.eid, Exam.name, Exam.date FROM Exam'
    with db.engine.connect() as conn:
        return conn.execute(text(sql)).all()

def get_exam_name_by_eid(eid):
    '''
    Return assignment name by given eid 'eid'
    '''
    return Exam.query.filter(Exam.eid == eid).first().name