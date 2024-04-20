import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pon.settings')

celery_app = Celery('pon')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'add-every-week': {
        'task': 'schedule.tasks.update_schedule',
        'schedule':  crontab(hour=0, minute=23, day_of_week='mon')
    },
}