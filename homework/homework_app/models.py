from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    reg_date = models.DateField()

    def __str__(self):
        return f'User {self.name} {self.email} {self.phone} {self.address}'


class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to='item_pic/', null=True, blank=True)

    def __str__(self):
        return f'Item {self.title} {self.description} {self.price}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Item, related_name="orders")
    total_price = models.DecimalField(max_digits=50, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.total_price}'
