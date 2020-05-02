from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from .models import Rate

__all__ = ('handlers',)


def rate_count(update, context):
    update.message.reply_text(f'Rate count: {Rate.objects.count()}')


handlers = [
    CommandHandler("rate", rate_count),
]
