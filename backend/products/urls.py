from django.urls import path, include

from products import views

urlpatterns = [
    path('product-list/', views.ProductsList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('event-list/', views.EventsList.as_view()),
path('events/<slug:category_slug>/<slug:event_slug>/', views.EventDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    #admin authntication
]
