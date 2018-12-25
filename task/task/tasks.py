from __future__ import absolute_import
import sys ,os
from users_service.models import User
# from task.users_service.models import User
from .celery import app


@app.task
def add_user(user):
    print('urra')
    user = User(first_name=user[0], last_name=user[1], email=user[2])
    user.save()