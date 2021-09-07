from django.contrib.auth import logout, views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import  logout
from .forms import LoginForm, RegisterForm
from django.shortcuts import render,redirect
from stocks.models import Stock_details
from mutualfunds.models import mutualfunds_details
from indices.models import indices_details
from forex.models import forex_details
from etf.models import etf_details
from crypto.models import crypto_details
from django.db.models import Sum
import itertools
class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'dashboard/login.html'
class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'dashboard/register.html'
    success_url = reverse_lazy('login')
def signout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request,'dashboard/home.html')
def analytics(request):
    user=request.user
    total_current_value=[]
    total_current_value.append(list(Stock_details.objects.filter(user=user).aggregate(Sum('current_value')).values()))
    total_current_value.append(list(mutualfunds_details.objects.filter(user=user).aggregate(Sum('current_value')).values()))
    total_current_value.append(list(indices_details.objects.filter(user=user).aggregate(Sum('current_value')).values()))
    total_current_value.append(list(forex_details.objects.filter(user=user).aggregate(Sum('current_value')).values()))
    total_current_value.append(list(etf_details.objects.filter(user=user).aggregate(Sum('current_value')).values()))
    total_current_value.append(list(crypto_details.objects.filter(user=user).aggregate(Sum('current_value')).values()))
    total_current_value=list(itertools.chain.from_iterable(total_current_value))
    for i in range (len(total_current_value)):
        if total_current_value[i]==None:
            total_current_value[i]=0
    total_gain=[]
    total_gain.append(list(Stock_details.objects.filter(user=user).aggregate(Sum('Overall_Gain')).values()))
    total_gain.append(list(mutualfunds_details.objects.filter(user=user).aggregate(Sum('Overall_Gain')).values()))
    total_gain.append(list(indices_details.objects.filter(user=user).aggregate(Sum('Overall_Gain')).values()))
    total_gain.append(list(forex_details.objects.filter(user=user).aggregate(Sum('Overall_Gain')).values()))
    total_gain.append(list(etf_details.objects.filter(user=user).aggregate(Sum('Overall_Gain')).values()))
    total_gain.append(list(crypto_details.objects.filter(user=user).aggregate(Sum('Overall_Gain')).values()))
    total_gain=list(itertools.chain.from_iterable(total_gain))
    for i in range (len(total_gain)):
        if total_gain[i]==None:
            total_gain[i]=0
    total_investment=[]
    total_investment.append(list(Stock_details.objects.filter(user=user).aggregate(Sum('invested_amount')).values()))
    total_investment.append(list(mutualfunds_details.objects.filter(user=user).aggregate(Sum('invested_amount')).values()))
    total_investment.append(list(indices_details.objects.filter(user=user).aggregate(Sum('invested_amount')).values()))
    total_investment.append(list(forex_details.objects.filter(user=user).aggregate(Sum('invested_amount')).values()))
    total_investment.append(list(etf_details.objects.filter(user=user).aggregate(Sum('invested_amount')).values()))
    total_investment.append(list(crypto_details.objects.filter(user=user).aggregate(Sum('invested_amount')).values()))
    total_investment=list(itertools.chain.from_iterable(total_investment))
    for i in range (len(total_investment)):
        if total_investment[i]==None:
            total_investment[i]=0
    
    return render(request,'dashboard/analytics.html',{'total_current_value':total_current_value,'total_gain':total_gain,'total_investment':total_investment})