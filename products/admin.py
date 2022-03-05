from django.contrib import admin

from .models import Tour, Product,Event,Ticket, Order, OrderItem
# Register your models here.


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name_tour', 'artist')
    prepopulated_fields = {'slug': ('name_tour','artist')} 
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name_event', 'status_event', 'city')
    prepopulated_fields = {'slug': ('name_event','city')} 
    list_filter=['date_event','city']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'event', 'price', 'stock')
    prepopulated_fields = {'slug': ('name_product',)} 
    list_filter=['date_added','price']
    search_fields = ['name_product']

@admin.register(Ticket)
class TickettAdmin(admin.ModelAdmin):
    list_display = ('name_ticket', 'event','price', 'stock')
    prepopulated_fields = {'slug': ('name_ticket',)} 
    list_filter=['date_added','price']
    search_fields = ['name_ticket']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_added')
    list_filter=['date_added']
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')