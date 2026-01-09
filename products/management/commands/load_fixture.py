from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load product fixture into the database'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'products.json')
        self.stdout.write(self.style.SUCCESS('Product fixture loaded successfully.'))