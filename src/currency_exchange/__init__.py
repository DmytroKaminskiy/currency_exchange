from .celery import app as celery_app
from .tel_bot import telegram

__all__ = ('celery_app', 'telegram')
