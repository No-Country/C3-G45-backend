from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView, ListCreateAPIView

from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .models import Product, Event, Tour, Ticket, Order
from .serializers import ProductSerializer, EventSerializer, TicketSerializer, OrderSerializer,OrderDetailSerializer,TourSerializer

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings



User=get_user_model()

class ToursList(ListAPIView):
    queryset= Tour.objects.all()
    serializer_class= TourSerializer

class EventsList(APIView):
    """Shows the list of events"""
    def get(self, request, format=None):
        events = Event.objects.all()[0:4]
        serializer = EventSerializer(events, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   

class ProductsList(ListCreateAPIView):
    """Shows the list of products"""
    search_fields = ['name_product','description']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(RetrieveAPIView):
    """Shows in detail the information of a product"""
    lookup_field="slug"
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

class TicketsList(ListCreateAPIView):
    """Shows the list of tickets"""
    search_fields = ['name_ticket','description']
    filter_backends = (filters.SearchFilter,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetail(RetrieveAPIView):
    """Shows in detail the information of a ticket"""
    lookup_field="slug"
    queryset= Ticket.objects.all()
    serializer_class= TicketSerializer

class OrdersList(APIView):
   # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    #permission_classes=[IsAuthenticated]#,IsAdminUser

    def get(self,request):
        orders=Order.objects.all()
        serializer=self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        user = request.user

        if serializer.is_valid():
            serializer.save(user=user)
            
            #Email confirmation
            customer={'username':user.first_name}
            subject = 'Purchase successful'
            message = 'Your purschase was successful'
            email_template='success_email.html'
            
            html_message = render_to_string(email_template, context=customer)
            recipient = request.user.email
            send_mail(subject, message,
              settings.EMAIL_HOST_USER, [recipient], 
              html_message=html_message, fail_silently=False)
            messages.success(request, 'Success!')

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class OrderIdView(GenericAPIView):
    """CRUD Order view with ID"""
    serializer_class=OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes=[IsAuthenticated]

    def get(self, request, order_id):
        order=get_object_or_404(Order,pk=order_id)        
        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self,request,order_id):
        order=get_object_or_404(Order,pk=order_id)
        serializer=self.serializer_class(instance=order,data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,order_id):
        order =get_object_or_404(Order,id=order_id)
        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserOrdersView(GenericAPIView):
    """ Get view order from user """
    serializer_class= OrderDetailSerializer 
    permission_classes= [IsAuthenticated]

    def get(self,request,user_id):
        user=User.objects.get(pk=user_id)
        orders=Order.objects.all().filter(user=user)
        serializer=self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

class UserOrderDetailView(GenericAPIView):
    serializer_class= OrderDetailSerializer
    permission_classes=[IsAuthenticated]

    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)
        order=Order.objects.all().filter(user=user).get(pk=order_id)
        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data,status=status.HTTP_200_OK)