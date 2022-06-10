from backend.models import *

# Utility functions to use for database operations:

# def db_instances(model):
#     object_list = model.objects.all()
#     return object_list

def validate_user(username, password):
    if (
        User.objects.filter(username__exact=username) 
        and 
        User.objects.filter(password__exact=password)
        ):
        return True
    else:
        return False

