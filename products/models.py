from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Tour(models.Model):
    """Tour details for the artist"""
    name_tour = models.CharField(max_length=255)
    artista= models.CharField(max_length=150, null=True)
    description= models.TextField(blank=True, null=True)
    tour_image=models.ImageField(upload_to='uploads/', blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name_tour

    def get_absolute_url(self):
        return f'/{self.name_tour.slug}/{self.slug}/'
    
    def get_image(self):
        if self.tour_image:
            return 'http://127.0.0.1:8000' + self.tour_image.url
        return ''


class Event(models.Model):
    """Each event has tickets and products to be sold"""

    EVENT_STATUS=(
        ('SOON','soon'),
        ('PRESALE','presale'),
        ('AVAILABLE','available'),
        ('SOLD OUT','sold out'),
        ('CANCELLED','cancelled')          
    )

    id_tour = models.ForeignKey(Tour, related_name='events', on_delete=models.CASCADE)
    name_event = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status_event= models.CharField(max_length=15, choices=EVENT_STATUS, null=True,default=EVENT_STATUS[0][0])
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_event= models.DateTimeField()
    city=models.CharField(max_length=255)
    location= models.CharField(max_length=255)
    image_event = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name_event
    
    def get_absolute_url(self):
        return f'/{self.id_tour.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image_event:
            return 'http://127.0.0.1:8000' + self.image_event.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url

        else:
            if self.image_event:
                self.thumbnail = self.make_thumbnail(self.image_event)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url

            else:
                return ''
    
    def make_thumbnail(self, image_event, size=(300, 200)):
        img = Image.open(image_event)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image_event.name)

        return thumbnail


class Product(models.Model):
    """Products for Events"""
    id_event_product = models.ForeignKey(Event, related_name='products', on_delete=models.CASCADE)
    name_product = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name_product
    
    def get_absolute_url(self):
        return f'/{self.id_event_product.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class Ticket(models.Model):
    """Tickets for Events """
    id_event_ticket = models.ForeignKey(Event, related_name='tickets', on_delete=models.CASCADE)
    name_ticket = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name_ticket
    
    def get_absolute_url(self):
        return f'/{self.id_event_ticket.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class Order(models.Model):
    """Purchased orders """
    id_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    # Items
    product_order= models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    #event_order=models.ForeignKey(Ticket, on_delete=models.CASCADE,null=True)
    
    # Quantity
    quantity_product=models.IntegerField(null=True)
    #quantity_event=models.IntegerField(null=True)
    
    ORDER_STATUS=(
        ('CREATED','created'),
        ('PENDING','pending'),
        ('PAID','paid'),
        ('COMPLETED','completed'),
        
    )

    order_status=models.CharField(max_length=25,choices=ORDER_STATUS,default=ORDER_STATUS[0][0])
    updated_at=models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        #{self.product_order} or {self.event_order}
        return f"<Order by {self.id_user}>"


class OrderItem(models.Model):
    id_order=models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE,null=True)
    id_product_order= models.ForeignKey(Product, related_name='items',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        #{self.product_order} or {self.event_order}
        return f"<Order {self.id_order}>"

class Ticket_Order(models.Model):
    id_order=models.ForeignKey(Order, related_name='tickets_order',on_delete=models.CASCADE,null=True)
    id_ticket_order= models.ForeignKey(Ticket, on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        #{self.product_order} or {self.event_order}
        return f"<Order {self.id_order}>"
    
    