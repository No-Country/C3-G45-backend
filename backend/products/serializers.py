from rest_framework import serializers

from .models import Category, Product, Event,Order

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
            "status_event",
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

class OrderSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
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
            "category"
        )
