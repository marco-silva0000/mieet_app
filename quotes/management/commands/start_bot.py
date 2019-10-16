from django.core.management.base import BaseCommand, CommandError
from django import conf 
from quotes.telegram_bot import Bot

class Command(BaseCommand):
    help = 'starts telegram bot'

    def handle(self, *args, **options):
        Bot(conf.settings.TELEGRAM_TOKEN).run()
