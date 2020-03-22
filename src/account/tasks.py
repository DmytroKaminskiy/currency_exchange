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
