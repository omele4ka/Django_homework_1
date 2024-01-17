from django.core.management.base import BaseCommand
from homework_app.models import Item


class Command(BaseCommand):
    help = 'create item'

    def handle(self, *args, **kwargs):
        item = Item(title='Some item', description='the best item', price=100.99, quantity=5)
        item.save()
        self.stdout.write(f'{item} is created')