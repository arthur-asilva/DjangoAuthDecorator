from os import access
from django.shortcuts import redirect
from apps.users.models import User, Permission

def ViewAccessControl(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        user = User.objects.get(id=args[0].session['user_id'])
        access = Permission.objects.values('view_access').filter(user=user)
        access_permission = False
        for view in access:
            if func.__name__ == view['view_access']:
                access_permission = True
        if not access_permission:
                    return redirect('../unauthorized_page/')
        return result
    return wrap