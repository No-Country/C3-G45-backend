from django.urls import path
from . import views

#Urls authentication
urlpatterns = [
    path('signup/',views.UserCreateView.as_view(),name='signup'),
]