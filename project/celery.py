import os
from celery import Celery

from celery.schedules import crontab    # Позволяет создавать задачу на точное определенное время

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'simpleapp.tasks.week_send_task',
        'schedule': crontab(),
    },
}

app.autodiscover_tasks()