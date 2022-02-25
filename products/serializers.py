from rest_framework import serializers
from .models import Product, Event, Order, Ticket, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name_product",
            "get_absolute_url",
            "description",
            "price",
            "stock",
            "get_image",
            "get_thumbnail"
        )

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "name_ticket",
            "get_absolute_url",
            "description",
            "price",
            "stock",
            "get_image",
            "get_thumbnail"
        )


class EventSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    tickets = TicketSerializer(many=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "name_event",
            "description",           
            "status_event",
            "get_image",
            "get_thumbnail",
            "date_event",
            "city",
            "location",
            "get_absolute_url",
            "products",
            "tickets",
        )

""" 
class Product_OrderSerializer(serializers.ModelSerializer):
    products= ProductSerializer()

    class Meta:
        model=Product_Order 
        fields=(
            "id",
            "products",
        )
 """


class OrderSerializer(serializers.ModelSerializer):
    product_order= ProductSerializer() #serializers.CharField()
    quantity_product=serializers.IntegerField()
    order_status=serializers.HiddenField(default="PENDING")
    
    class Meta:
        model=Order 
        fields=(
            #'id_user',
            'id',
            'quantity_product',
            'order_status',
            'product_order',
        )

class OrderDetailSerializer(serializers.ModelSerializer):
    product_order= ProductSerializer() # serializers.CharField() 
    quantity_product=serializers.IntegerField()
    order_status=serializers.CharField(default="PENDING")
    date_added= serializers.DateTimeField()
    updated_at= serializers.DateTimeField()

    class Meta:
        model=Order 
        fields=(
            'id',
            'quantity_product',
            'order_status',
            'product_order',
            'date_added',
            'updated_at',
        )
