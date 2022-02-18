from django.urls import path, include

from products import views

urlpatterns = [
    path('product-list/', views.ProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('event-list/', views.EventsList.as_view()),
]