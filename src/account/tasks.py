from celery import shared_task


@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task()
def send_email_async(subject, email, body):
    send_email()
