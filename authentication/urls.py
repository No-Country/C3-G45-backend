from django.urls import path
from . import views

#Urls authentication
urlpatterns = [
    path('signup/',views.UserCreateView.as_view(),name='signup'),
    #path(r'users/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', views.UserDetail.as_view(), name='user'),
    path('user/<slug:slug>/', views.UserDetail.as_view(), name='user'),

]