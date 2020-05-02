from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from .models import User

__all__ = ('handlers',)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def show_arguments(update, context):
    user_says = " ".join(context.args)
    update.message.reply_text(user_says)


def echo(update, context):
    update.message.reply_text(f'User Count: {User.objects.count()}')


handlers = [
    CommandHandler("start", start),
    CommandHandler("args", show_arguments),
    CommandHandler("help", help),
    MessageHandler(Filters.text, echo),
]
