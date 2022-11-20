from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.CharField(max_length=350,null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.name

class Vehicles(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.CharField(max_length=350,null=True,blank=True)
    quanity=models.IntegerField(null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    millage=models.IntegerField(null=False,blank=False)
    bikengine=models.TextField(max_length=500,null=False,blank=False)
    maxpower=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return  self.name

class Company(models.Model):
    cimage=models.CharField(max_length=350,null=True,blank=True)
    coname=models.CharField(max_length=150,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
   