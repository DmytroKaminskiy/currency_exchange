from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

__all__ = ('handlers',)


def start(update, context):
    update.message.reply_text('Hi!')


def help(update, context):
    update.message.reply_text('Help!')


handlers = [
    CommandHandler("start", start),
    CommandHandler("help", help),
]
