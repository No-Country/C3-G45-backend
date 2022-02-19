from django.contrib import admin

from .models import Category, Product,Event, Order
# Register your models here.

admin.site.register(Order)
#admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Event)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','artista']
    list_filter=['id','artista']