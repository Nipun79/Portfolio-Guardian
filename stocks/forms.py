from django.forms import fields
from .models import Stock_details
from django import forms
import datetime


class Stock_details_form(forms.ModelForm):
    class Meta:
        model = Stock_details
        fields=["companyName","qty","current_price","avg_price","current_value","invested_amount","Today_Gain","Overall_Gain","Buy_Sell","date"]
      