from flask import session
from modules.models import *

def get_assignment_remark_req():
    '''
    Return assignment regrade request (name, (new) mark, comment from instructor) 
    for current student by "session['username']"
    '''
    ass_req = Assignment_Regrade_Request.query.all()
    cur_utorid = get_utorid_by_username(session['username'])
    ret = []
    for item in ass_req:
        dict = {'name': Assignment.query.filter(Assignment.aid == item.aid).first().name,
            'mark': Assignment_Grade.query.filter(Assignment_Grade.aid == item.aid and\
                                                  Assignment_Grade.sid == cur_utorid).first().grade,
            'comment': item.comment}
        ret.append(dict)
    return ret

def get_exam_remark_req():
    '''
    Return exam regrade request (name, (new) mark, comment from instructor) for 
    current student by "session['username']"
    '''
    exam_req = Exam_Regrade_Request.query.all()
    cur_utorid = get_utorid_by_username(session['username'])
    ret = []
    for item in exam_req:
        dict = {'name': Exam.query.filter(Exam.eid == item.eid).first().name,
            'mark': Exam_Grade.query.filter(Exam_Grade.eid == item.eid and \
                                            Exam_Grade.sid == cur_utorid).first().grade,
            'comment': item.comment}
        ret.append(dict)
    return ret