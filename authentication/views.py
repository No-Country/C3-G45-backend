from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .  import serializers

from django.contrib.auth import get_user_model

User=get_user_model()

# Create your views here.
class UserCreateView(generics.GenericAPIView):
    serializer_class=serializers.UserCreationSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetail(RetrieveAPIView):
    """Shows in detail the information of a user"""

    permission_classes=[IsAuthenticated]

    lookup_field="slug"
    queryset= User.objects.all()
    serializer_class= serializers.UserDetail