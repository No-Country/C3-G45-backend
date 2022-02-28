from django.http import Http404
from django.db.models import Q
from django.shortcuts import render,get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView, ListCreateAPIView

from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .models import Product, Event, Tour, Ticket, Order
from .serializers import ProductSerializer, EventSerializer, TicketSerializer, OrderSerializer, OrderDetailSerializer

from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import filters


class EventsList(APIView):
    """Shows the list of events"""
    def get(self, request, format=None):
        events =Event.objects.all()[0:4]
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
        
class ProductsList(ListAPIView):
    """Shows the list of products"""
    search_fields = ['name_product','description']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveAPIView):
    """Shows in detail the information of a product"""
    lookup_field="name_product"
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

class TicketsList(APIView):
    def get(self, request, format=None):
        tickets = Ticket.objects.all()[0:4]
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)


class TicketDetail(RetrieveAPIView):
    """Shows in detail the information of a ticket"""
    lookup_field="name_ticket"
    queryset= Ticket.objects.all()
    serializer_class= TicketSerializer


class OrderList(ListCreateAPIView):
    queryset= Order.objects.all()
    serializer_class= OrderSerializer

""" 
class OrderCreateListView(APIView):
    serializer_class= OrderSerializer
    queryset= Order.objects.all()

    #permission_classes=[IsAuthenticated]

    def get(self, request):
        orders= Order.objects.all()
        serializer=self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
    
        serializer = self.serializer_class(data=request.data, many=True)
        user=request.user

        if serializer.is_valid():
            serializer.save(id_user=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

class OrderDetailView(GenericAPIView):
    
    serializer_class=OrderDetailSerializer
    #permission_classes=[IsAuthenticated]

    def get(self, request, order_id):
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put (self, request, order_id):
        order=get_object_or_404(Order,pk=order_id)
        
        serializer=self.serializer_class(instance=order,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, order_id):
        pass

 """