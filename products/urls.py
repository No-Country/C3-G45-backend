from django.urls import path, include

from products import views

urlpatterns = [
    # tours path
    path('tour-list/', views.ToursList.as_view(), name='tours'),

    # events path
    path('event-list/', views.EventsList.as_view(), name='events'),

    #product paths
    path('product-list/', views.ProductsList.as_view(), name='products'),    
    path("products/<slug:slug>/", views.ProductDetail.as_view(), name="product"),

    #ticket paths
    path('ticket-list/', views.TicketsList.as_view(), name='tickets'),
    path('tickets/<slug:slug>/', views.TicketDetail.as_view(),name='ticket_detail'),

    #order paths
   # path('order/', views.OrderList.as_view(), name='order'),
   # path('order-create/', views.OrderCreateListView.as_view(), name='order-create'),
    #path('order/<int:order_id>/',views.OrderDetailView.as_view(),name='order_detail'),
    #path('checkout/', views.checkout, name="checkout"),
    path('order-list/', views.OrdersList.as_view(), name="order_list"),
    #path('orders/', views.Orders.as_view(), name="orders"),

    path('order-view/', views.OrderView.as_view(), name="orderview"),
    path('order/<int:order_id>/', views.OrderIdView.as_view(), name="order_detail"),
    
    #user orders
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name="users_orders"),
    path('user/<int:user_id>/order/<int:order_id>/', views.UserOrderDetailView.as_view(), name="users_order_detail"),






]
