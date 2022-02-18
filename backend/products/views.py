from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Event
from .serializers import ProductSerializer, EventSerializer


class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class EventsList(APIView):
    def get(self, request, format=None):
        events =Event.objects.all()[0:4]
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
        
class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class EventDetail(APIView):
    def get_object(self, category_slug, event_slug):
        try:
            return Event.objects.filter(category__slug=category_slug).get(slug=event_slug)
        except Event.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, event_slug, format=None):
        event = self.get_object(category_slug, event_slug)
        serializer = EventSerializer(event)
        return Response(serializer.data)
