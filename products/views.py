from django.http import Http404
from django.shortcuts import render,get_object_or_404

from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView, ListCreateAPIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .models import Product, Event, Tour, Ticket, Order
from .serializers import ProductSerializer, EventSerializer, TicketSerializer, OrderSerializer,OrderDetailSerializer

from django.contrib.auth import get_user_model

User=get_user_model()

class EventsList(APIView):
    """Shows the list of events"""
    def get(self, request, format=None):
        events = Event.objects.all()[0:4]
        serializer = EventSerializer(events, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    """ def post(self, request, format=None):
        serializer = EventSerializer(request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)
 """
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            print(f"\n {serializer.data}")

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
    lookup_field="name_product"
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

class TicketsList(APIView):
    """Shows the list of tickets"""
    search_fields = ['name_ticket','description']
    filter_backends = (filters.SearchFilter,)
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetail(RetrieveAPIView):
    """Shows in detail the information of a ticket"""
    lookup_field="name_ticket"
    queryset= Ticket.objects.all()
    serializer_class= TicketSerializer

class OrdersList(APIView):
   # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderView(GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes=[IsAuthenticated,IsAdminUser]

    def get(self,request):
        orders=Order.objects.all()
        serializer=self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            #print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class OrderIdView(GenericAPIView):
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
    serializer_class= OrderDetailSerializer 
    permission_classes= [IsAuthenticated,IsAdminUser]

    def get(self,request,user_id):
        user=User.objects.get(pk=user_id)

        orders=Order.objects.all().filter(user=user)
        serializer=self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

class UserOrderDetailView(GenericAPIView):
    serializer_class= OrderDetailSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]

    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)

        order=Order.objects.all().filter(user=user).get(pk=order_id)
        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

""" 
class OrderList(ListCreateAPIView):
    queryset= Order.objects.all()
    serializer_class= OrderSerializer


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
         """
""" 
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
"""
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 """

""" 
#Class replaced by OrderView
class Orders(ListCreateAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
 """