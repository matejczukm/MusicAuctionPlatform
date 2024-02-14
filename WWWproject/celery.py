# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

celery_app = Celery('WWWproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WWWproject.settings')
celery_app.conf.broker_url = 'memory://'

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'create-orders': {
        'task': 'WWWproject.tasks.create_orders_for_expired_auctions',
        'schedule': crontab(),
    },
}
