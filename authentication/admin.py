from django.contrib import admin
from .models import User

# Register your models here.

admin.site.register(User)

""" 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    listdisplay = ('username', 'first_name','email')
    #prepopulated_fields = {'slug': ('name_tour','artist')} 
    """