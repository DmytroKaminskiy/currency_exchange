import requests
import os

from celery import shared_task
from django.core.mail import send_mail
from django.urls import reverse


@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task()
def send_email_async(subject, email, body):
    send_email()


@shared_task()
def send_activation_code_async(email_to, code):
    path = reverse('account:activate', args=(code, ))

    send_mail(
        'Your activation code',
        f'http://127.0.0.1:8001{path}',
        'fenderoksp@gmail.com',
        [email_to],
        fail_silently=False,
    )


@shared_task()
def send_tel_message():

    bot_api_key = os.environ['TELEGRAM_BOT_API_KEY']
    channel_name = '@CurrencyExchangeBotHillel'
    message = 'Hello @/?World'

    url = f'https://api.telegram.org/bot{bot_api_key}/sendMessage'

    params = {
        'chat_id': channel_name,
        'text': message,  # TODO message, email, Name
    }

    # logs parameters send, get from API
    print(requests.get(url, params=params).json())
