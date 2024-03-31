from modules.models import *

def get_id_by_name(name):
    # Assuming that no instructor have the same name
    for instructor in Instructor.query.all():
        if name in instructor.name.lower():
            return instructor.utorid
    return -1
