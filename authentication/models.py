from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email should be provided"))
        
        email=self.normalize_email(email)
        new_user=self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()

        return new_user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff=True"))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser should have is_superuser=True'))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser should have is_active=True'))


        return self.create_user(email,password,**extra_fields)


class User(AbstractUser):
    username=models.CharField(_('Username'), max_length=40,unique=True)
    first_name=models.CharField(_('First Name'), max_length=40,unique=False)
    last_name=models.CharField(_('Last Name'), max_length=40,unique=False)
    email=models.EmailField(_('Email'), max_length=80,unique=True)
    created_at=models.DateTimeField(_('Date'),auto_now_add=True)
    slug = models.SlugField(unique=True, null=True)

    REQUIRED_FIELDS=['username','first_name']
    USERNAME_FIELD='email'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.email)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"User {self.email}"