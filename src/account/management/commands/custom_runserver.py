from datetime import datetime

from django.core.management.base import BaseCommand

from currency_exchange import telegram


class Command(BaseCommand):
    help = "Starts a telegram app."

    def handle(self, *args, **options):
        self.stdout.write("Performing system checks...\n\n")
        self.check(display_num_errors=True)
        self.check_migrations()
        now = datetime.now().strftime('%B %d, %Y - %X')
        self.stdout.write(now)
        telegram()
