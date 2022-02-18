from django.contrib import admin

from .models import Category, Product,Event, Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Event)
