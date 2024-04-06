from flask import session
from modules.models import *

def get_assignment_remark_req():
    '''
    Return assignment regrade request info (reqid, sid, aid, desc, comment) 
    '''
    return Assignment_Regrade_Request.query.all()

def get_assignment_remark_req_by_cur_student():
    '''
    Return assignment regrade request (name, (new) mark, comment from instructor) 
    for current student by "session['username']"
    '''
    ass_req = get_assignment_remark_req()
    cur_utorid = get_utorid_by_username(session['username'])
    ret = []
    for item in ass_req:
        if item.sid != cur_utorid:
            continue

        dict = {'name': Assignment.query.filter(Assignment.aid == item.aid).first().name,
            'mark': Assignment_Grade.query.filter(Assignment_Grade.aid == item.aid and\
                                                  Assignment_Grade.sid == cur_utorid).first().grade,
            'comment': item.comment}
        ret.append(dict)
    return ret

def get_exam_remark_req():
    '''
    Return exam regrade request info (reqid, sid, eid, desc, comment) 
    '''
    return Exam_Regrade_Request.query.all()

def get_exam_remark_req_by_cur_student():
    '''
    Return exam regrade request (name, (new) mark, comment from instructor) for 
    current student by "session['username']"
    '''
    exam_req = get_exam_remark_req()
    cur_utorid = get_utorid_by_username(session['username'])
    ret = []
    for item in exam_req:
        if item.sid != cur_utorid:
            continue

        dict = {'name': Exam.query.filter(Exam.eid == item.eid).first().name,
            'mark': Exam_Grade.query.filter(Exam_Grade.eid == item.eid and \
                                            Exam_Grade.sid == cur_utorid).first().grade,
            'comment': item.comment}
        ret.append(dict)
    return ret

def add_remark_comment(remark_request_info):
    '''
    Add a comment to the grade request
    '''
    if remark_request_info['assessment-type'] == 'a':
        remark_request = Assignment_Regrade_Request.query.filter(Assignment_Regrade_Request.reqid == remark_request_info['id']).first()
        print('Here is Remark Request Info (Assignment): ', remark_request.reqid, remark_request.aid, remark_request.sid)
        remark_request.comment = remark_request_info['desc']
        db.session.commit()
    elif remark_request_info['assessment-type'] == 'e':
        remark_request = Exam_Regrade_Request.query.filter(Exam_Regrade_Request.reqid == remark_request_info['id']).first()
        print('Here is Remark Request Info (Exam): ', remark_request.reqid, remark_request.eid, remark_request.sid)
        remark_request.comment = remark_request_info['desc']
        db.session.commit()