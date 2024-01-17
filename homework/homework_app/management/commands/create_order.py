from django.core.management.base import BaseCommand
from homework_app.models import Order, Item


class Command(BaseCommand):
    help = 'create order'


    def handle(self, *args, **kwargs):
        order = Order(user_id=1, total_price='500.00')
        order.save()
        item_id = 1
        item = Item.objects.get(pk=item_id)
        order.item.add(item)
        order.save()
        self.stdout.write(f'{order} is created')