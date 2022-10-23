
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .manager import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True,blank=True,null=True)
    first_name=models.CharField(max_length=255,blank=True,null=True)
    last_name=models.CharField(max_length=255,blank=True,null=True)
    phone=models.CharField(max_length=255,blank=True,null=True)
    image=models.ImageField(null=True,blank=True,default='default.png')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    def __str__(self):
        return self.name
class Book(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    image=models.ImageField(null=True,blank=True,default='default.png')
    category=models.ManyToManyField(Category)
    transaction=models.ManyToManyField('Transaction')
    store=models.ForeignKey('Store',on_delete=models.CASCADE,null=True,blank=True)
    rating=models.FloatField(null=True,blank=True,default='5')
    def __str__(self):
        return self.name
class Transaction(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    def __str__(self):
        return self.name
class Store(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    email=models.EmailField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,default='default.png')
    phone=models.CharField(max_length=255,null=False,blank=False)
    city=models.ForeignKey('City',on_delete=models.CASCADE,null=True,blank=True)
    rating=models.FloatField(null=True,blank=True,default="5")
    review=models.IntegerField(null=True,blank=True,default=0)
    def __str__(self):
        return self.name
class City(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    def __str__(self):
        return self.name
