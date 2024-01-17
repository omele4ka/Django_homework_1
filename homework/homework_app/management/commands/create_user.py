from django.core.management.base import BaseCommand
from homework_app.models import User


class Command(BaseCommand):
    help = 'create user'

    def handle(self, *args, **kwargs):
        user = User(name='Yarik', email='yarik@gmail.com', phone='123', address='QRoo', reg_date='2024-01-17')
        user.save()
        self.stdout.write(f'User {user} is created')