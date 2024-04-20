import logging

from celery import shared_task
from .helpers import TasksHelper
from db_app.models import User

@shared_task
def update_schedule():
    users = User.objects.all()
    helper = TasksHelper()
    for user in users:
        logging.error(user.group_id)
        if user.group_id and user.group_id != 0:
            helper.schedule_to_tasks(user)
