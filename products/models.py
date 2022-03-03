from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Tour(models.Model):
    """Tour details for the artist"""
    name_tour = models.CharField(max_length=255)
    artist= models.CharField(max_length=150, null=True, default="Dua Lipa")
    description= models.TextField(blank=True, null=True)
    tour_image=models.ImageField(upload_to='tours/', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name_tour

class Event(models.Model):
    """Each event has tickets and products to be sold"""

    EVENT_STATUS=(
        ('SOON','soon'),
        ('PRESALE','presale'),
        ('AVAILABLE','available'),
        ('SOLD OUT','sold out'),
        ('CANCELLED','cancelled')          
    )

    tour = models.ForeignKey(Tour, related_name='events', on_delete=models.CASCADE, default=-1)
    name_event = models.CharField(max_length=255)
    city=models.CharField(max_length=60)
    location= models.CharField(max_length=255)
    date_event= models.DateTimeField()
    status_event= models.CharField(max_length=15, choices=EVENT_STATUS, null=True,default=EVENT_STATUS[0][0])
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    image_event = models.ImageField(upload_to='events/', blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name_event

class Product(models.Model):
    """Products for Events"""
    event = models.ForeignKey(Event, related_name='products', on_delete=models.CASCADE, default=-1)
    name_product = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    stock=models.IntegerField(blank=True, null=True, default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name_product
    
class Ticket(models.Model):
    """Tickets for Events """
    id_event_ticket = models.ForeignKey(Event, related_name='tickets', on_delete=models.CASCADE, default=-1)
    name_ticket = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='tickets/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name_ticket
    
class Order(models.Model):
    """Purchased orders """
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    #updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return f"Order by {self.user}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE,null=True)
    product= models.ForeignKey(Product, related_name='items',on_delete=models.CASCADE,null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,blank=True, null=True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        #return '%s' % self.id
        return f"Id {self.id} {self.product} by {self.order.user} "
