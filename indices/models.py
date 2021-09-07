from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import User



class indices_details(models.Model):
    user =models.ForeignKey('dashboard.Account', on_delete= models.CASCADE,null=True)
    Name=models.CharField(max_length=100,default="")
    avg_price=models.IntegerField(default=0)
    qty=models.IntegerField(default=0)
    invested_amount=models.FloatField(default=0)
    current_price=models.FloatField(default=0)
    current_value=models.FloatField(default=0)
    Overall_Gain=models.FloatField(default=0)
    CHOICES=('Buy','Sell')
    buy_sell_choice = (
		('Buy', 'Buy'),
		('Sell', 'Sell'),
	)
    Buy_Sell = models.CharField(default="None",max_length=50, blank=True, null=True, choices=buy_sell_choice)
    date=models.CharField(max_length=255,default="Date")