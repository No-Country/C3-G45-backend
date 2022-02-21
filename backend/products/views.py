from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product, Event, Tour, Ticket
from .serializers import ProductSerializer, EventSerializer, TicketSerializer

class EventsList(APIView):
    def get(self, request, format=None):
        events =Event.objects.all()[0:4]
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
        

class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class TicketsList(APIView):
    def get(self, request, format=None):
        tickets = Ticket.objects.all()[0:4]
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)