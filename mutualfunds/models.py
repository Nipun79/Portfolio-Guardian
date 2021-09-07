from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User



class mutualfunds_details(models.Model):
    user =models.ForeignKey('dashboard.Account', on_delete= models.CASCADE,null=True)
    Name=models.CharField(max_length=100,default="")
    avg_price=models.IntegerField(default=0)
    qty=models.IntegerField(default=0)
    invested_amount=models.FloatField(default=0)
    current_price=models.FloatField(default=0)
    current_value=models.FloatField(default=0)
    Overall_Gain=models.FloatField(default=0)
    date=models.CharField(max_length=25,default="None")