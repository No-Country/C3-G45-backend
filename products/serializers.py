from rest_framework import serializers
from .models import Product, Event, Order, Ticket, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    #id_event_product=serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = (
            "id",
            "name_product",
            "description",
            "price",
            "stock",
            "image"
        )

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "name_ticket",
            "description",
            "price",
            "stock",
            "image"
        )

class EventSerializer(serializers.ModelSerializer):
    products =  ProductSerializer(many=True)
    tickets = TicketSerializer(many=True)
   # id_tour = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = (
            "id",
            "name_event",
            "description",           
            "status_event",
            "image_event",
            "date_event",
            "city",
            "location",
            "products",
            "tickets",
 )

class TourSerializer(serializers.ModelSerializer):
    events =  EventSerializer(many=True)
    
    class Meta:
        model = Event
        fields = ('__all__')

class OrderItemSerializer(serializers.ModelSerializer):   
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "items",
        )
  
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
            
        return order

class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    date_added = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "date_added",
            "items",
        )
    
    