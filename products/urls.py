from django.urls import path, include

from products import views

urlpatterns = [
    # events path
    path('event-list/', views.EventsList.as_view()),

    #product paths
    path('product-list/', views.ProductsList.as_view()),
    path("products/<slug:name_product>/", views.Product.as_view(), name="product"),
    #path('products/<slug:event_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),

    #ticket paths
    path('ticket-list/', views.TicketsList.as_view()),
    #path('tickets/<slug:event_slug>/<slug:ticket_slug>/', views.TicketDetail.as_view()),

    #order paths
    path('order/', views.OrderCreateListView.as_view(), name='order'),
    path('order/<int:order_id>/',views.OrderDetailView.as_view(),name='order_detail'),

    #path('products/<slug:event_slug>/', views.TourDetail.as_view()),
    #admin authntication
]
