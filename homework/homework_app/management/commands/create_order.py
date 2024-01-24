from django.contrib.admin import options
from django.core.management.base import BaseCommand, CommandParser
from homework_app.models import Order, Item, User


class Command(BaseCommand):
    help = 'create order'


    def handle(self, *args, **kwargs):
        def add_arguments(self, parser: CommandParser):
            parser.add_argument('user_id', type=int, help='user id')
            parser.add_argument('item_id', type=int, help='item id')

        def handle(self, *args, **kwargs):
            user_id = options['user_id']
            item_id = options['item_id']

            user = User.objects.get(id=user_id)
            item = Item.objects.get(id=item_id)

            order = Order(
                user=user,
                item=item,
                total_sum=item.price * item.quantity
            )

            order.save()
            self.stdout.write(f'User {user.name} made a new order {order}')


