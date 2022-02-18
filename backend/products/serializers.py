from rest_framework import serializers

from .models import Category, Product, Event

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
            "status",
            "get_image",
            "get_thumbnail"
        )

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "date_event",
            "event_site",
            "price",
            "stock",
            "status",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    events = EventSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "artista",
            "get_absolute_url",
            "products",
            "events"
        )