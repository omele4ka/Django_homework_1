from django.contrib import admin
from .models import User, Item, Order


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price']


admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
