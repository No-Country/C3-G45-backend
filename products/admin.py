from django.contrib import admin

from .models import Tour, Product,Event,Ticket, Order
# Register your models here.

admin.site.register(Order)
admin.site.register(Tour)
admin.site.register(Ticket)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name_event', 'status_event', 'city')
    prepopulated_fields = {'slug': ('name_event','city')} 
    list_filter=['date_event','city']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price', 'stock')
    prepopulated_fields = {'slug': ('name_product',)} 
    list_filter=['date_added','price']
    search_fields = ['name_product']




