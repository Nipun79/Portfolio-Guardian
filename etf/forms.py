from django.forms import fields
from .models import etf_details
from django import forms



class etf_details_form(forms.ModelForm):
    class Meta:
        model = etf_details
        fields=["Name","qty","current_price","avg_price","current_value","invested_amount","Overall_Gain","Buy_Sell","date"]