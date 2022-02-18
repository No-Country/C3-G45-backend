from django.contrib import admin

from .models import Category, Product,Event,Status
# Register your models here.

admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Product)
admin.site.register(Event)
