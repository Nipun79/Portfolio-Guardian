from django.shortcuts import render,redirect
from .models import crypto_details
from .forms import crypto_details_form
import json,requests
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def crypto_list(request):
    if request.user.is_authenticated:
        user = request.user
        context={'crypto_list':crypto_details.objects.filter(user=user),
        'total_investment':crypto_details.objects.filter(user=user).aggregate(Sum('current_value')),
        'Overall_Gain': crypto_details.objects.filter(user=user).aggregate(Sum('Overall_Gain'))
        }
        #context={'crypto_list':crypto_details.objects.all()}
        return render(request,"crypto/crypto_list.html",context)
@login_required(login_url='login')
def crypto_form(request,id=0):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "GET":
            if id == 0:
                form = crypto_details_form()
            else:
                crypto= crypto_details.objects.get(pk=id)
                form = crypto_details_form(instance=crypto)
            return render(request, 'crypto/crypto_form.html', {'form': form})
        else:
            if id == 0:
                form = crypto_details_form(request.POST)
            else:
                crypto = crypto_details.objects.get(pk=id)
                form = crypto_details_form(request.POST,instance=crypto)
            if form.is_valid():
                saveform=form.save(commit=False)
                saveform.user=user
                saveform.save()
                
            return redirect('/crypto/list')
def crypto_delete(request,id):
    if request.user.is_authenticated:
        user = request.user
        crypto = crypto_details.objects.get(pk=id)
        crypto.delete()
        return redirect('/crypto/list')

@login_required(login_url='login')   
def crypto_edit(request,id):
    if request.method == "POST":
        crypto = crypto_details.objects.get(pk=id)
        form = crypto_details_form(request.POST,instance= crypto) 
        if form.is_valid():
            form.save()
        return redirect('/crypto/list')
    else:
        crypto = crypto_details.objects.get(pk=id)
        form = crypto_details_form(instance=crypto)
        return render(request,"crypto/crypto_edit.html",{'crypto':crypto})
@login_required(login_url='login')   
def search_crypto(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            ticker=request.POST['ticker']
            api_request=requests.get("https://api.twelvedata.com/time_series?symbol="+ticker+"&previous_close=true&dp=2&outputsize=1&interval=1min&apikey=44a7b9d780db42aeb04f68def28749b5")
            try:
                api=json.loads(api_request.content) 
                json.dumps(api)
            except Exception as e:
                api="Error"
            return render(request,'crypto/crypto_form.html',{'api':api})
        else:
            return render(request,'crypto/crypto_form.html',{'ticker':""})