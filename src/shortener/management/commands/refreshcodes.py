# refreshcodes is the command name & this file's name and is used as:
# python manage.py refreshcodes

from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortUrl

class Command(BaseCommand):
    help = 'Refreshes all the shortcodes, in the database'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
    	return ShortUrl.objects.refresh_shortcodes()