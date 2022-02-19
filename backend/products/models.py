from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
class Category(models.Model):
    # tour/gira
    name = models.CharField(max_length=255)
    artista= models.CharField(max_length=255, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS_PRODUCT=(
        ('DISPONIBLE', 'disponible'),
        ('AGOTADO','agotado'),
        
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField(blank=True, null=True)
    status_product= models.CharField(max_length=20, choices=STATUS_PRODUCT, default=STATUS_PRODUCT[0][0])
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
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


class Event(models.Model):
    EVENT_STATUS=(
        ('PRONTO','pronto'),
        ('PREVENTA','preventa'),
        ('DISPONIBLE','disponible'),
        ('AGOTADO','agotado'),
        ('SUSPENDIDO','suspendido')          
    )
    category = models.ForeignKey(Category, related_name='events', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField(blank=True, null=True)
    status_event= models.CharField(max_length=15, choices=EVENT_STATUS, null=True,default=EVENT_STATUS[0][0])
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='events/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_event= models.DateTimeField()
    event_site= models.CharField(max_length=255)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
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
    customer=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product_order= models.ForeignKey(Product, on_delete=models.CASCADE)
    #event_order=models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity_product=models.IntegerField()
    #quantity_event=models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        #{self.product_order} or {self.event_order}
        return f"<Order  by {self.customer}>"
    
    