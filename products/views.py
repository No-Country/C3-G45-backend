from django.http import Http404
from django.db.models import Q
from django.shortcuts import render,get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView

from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .models import Product, Event, Tour, Ticket, Order
from .serializers import ProductSerializer, EventSerializer, TicketSerializer, OrderSerializer, OrderDetailSerializer

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

class Product(RetrieveAPIView):
    lookup_field="name_product"
    queryset= Product.objects.all()
    serializer_class= ProductSerializer


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
    """ View class for displaying the order in detail"""
    
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