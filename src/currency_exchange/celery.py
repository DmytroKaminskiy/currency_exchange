import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_exchange.settings')

app = Celery('currency_exchange')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
