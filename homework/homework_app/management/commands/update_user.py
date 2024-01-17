from django.core.management.base import BaseCommand
from homework_app.models import User


class Command(BaseCommand):
    help = 'Update user by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID of the user to update')
        parser.add_argument('name', type=str, help='Name of the user to update')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f'{name} updated')