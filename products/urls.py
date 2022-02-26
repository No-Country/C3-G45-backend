from django.urls import path, include

from products import views

urlpatterns = [
    # events path
    path('event-list/', views.EventsList.as_view()),

    #product paths
    path('product-list/', views.ProductsView.as_view()),    
    path("products/<slug:name_product>/", views.ProductDetail.as_view(), name="product"),

    #ticket paths
    path('ticket-list/', views.TicketsList.as_view()),
    path('tickets/<slug:name_ticket>/', views.TicketDetail.as_view()),

    #order paths
    path('order/', views.OrderCreateListView.as_view(), name='order'),
    path('order/<int:order_id>/',views.OrderDetailView.as_view(),name='order_detail'),

]
