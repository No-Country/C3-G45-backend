from django.urls import path, include

from products import views

urlpatterns = [
    # events path
    path('event-list/', views.EventsList.as_view(), name='events'),

    #product paths
    path('product-list/', views.ProductsList.as_view(), name='products'),    
    path("products/<slug:name_product>/", views.ProductDetail.as_view(), name="product"),
    #path('products/search', views.search),

    #ticket paths
    path('ticket-list/', views.TicketsList.as_view(), name='tickets'),
    path('tickets/<slug:name_ticket>/', views.TicketDetail.as_view(),name='ticket_detail'),

    #order paths
   # path('order/', views.OrderList.as_view(), name='order'),
   # path('order-create/', views.OrderCreateListView.as_view(), name='order-create'),
    #path('order/<int:order_id>/',views.OrderDetailView.as_view(),name='order_detail'),
    path('checkout/', views.checkout, name="checkout"),
    path('order-list/', views.OrdersList.as_view(), name="checkout"),
    path('orders/', views.Orders.as_view(), name="orders"),

    path('order-view/', views.OrderView.as_view(), name="orderview"),
    path('order/<int:order_id>/', views.OrderIdView.as_view(), name="order_detail"),




]
