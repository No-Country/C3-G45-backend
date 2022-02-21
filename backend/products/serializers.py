from rest_framework import serializers
from .models import Tour, Product, Event,Order


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
        model = Product
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

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "stock",
            "status_product",
            "get_image",
            "get_thumbnail"
        )

class TourSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    events = EventSerializer(many=True)

    class Meta:
        model = Tour
        fields = (
            "id",
            "name",
            "artista",
            "get_absolute_url",
            "products",
            "events"
        )

class OrderSerializer(serializers.ModelSerializer):
    tour = TourSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "curtomer",
            "product_order",
            "event_order",
            "quantity_event",
            "quantity_product",
            "created_at",
            "updated_at",
            "our"
        )
 """