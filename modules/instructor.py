from modules.models import *

def get_id_by_name(name):
    # Assuming that no instructor have the same name
    for instructor in Login.query.filter(Login.user_type == 'instructor').all():
        if name in instructor.name.lower():
            return instructor.utorid
    return -1
