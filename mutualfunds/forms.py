from django.forms import fields
from .models import mutualfunds_details
from django import forms



class mutualfunds_details_form(forms.ModelForm):
    class Meta:
        model = mutualfunds_details
        fields=["Name","qty","current_price","avg_price","current_value","invested_amount","date","Overall_Gain"]