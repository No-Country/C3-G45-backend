from django.contrib import admin

from .models import Tour, Product,Event,Ticket, Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Tour)
admin.site.register(Ticket)
admin.site.register(Product)


""" @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','artista']
    list_filter=['id','artista'] """