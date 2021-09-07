from django.shortcuts import render,redirect
from .models import forex_details
from .forms import forex_details_form
import json,requests
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def forex_list(request):
    if request.user.is_authenticated:
        user = request.user
        context={'forex_list':forex_details.objects.filter(user=user),
        'total_investment':forex_details.objects.filter(user=user).aggregate(Sum('current_value')),
        'Overall_Gain': forex_details.objects.filter(user=user).aggregate(Sum('Overall_Gain'))
        }
        #context={'forex_list':forex_details.objects.all()}
        return render(request,"forex/forex_list.html",context)
@login_required(login_url='login')
def forex_form(request,id=0):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "GET":
            if id == 0:
                form = forex_details_form()
            else:
                forex= forex_details.objects.get(pk=id)
                form = forex_details_form(instance=forex)
            return render(request, 'forex/forex_form.html', {'form': form})
        else:
            if id == 0:
                form = forex_details_form(request.POST)
            else:
                forex = forex_details.objects.get(pk=id)
                form = forex_details_form(request.POST,instance=forex)
            if form.is_valid():
                saveform=form.save(commit=False)
                saveform.user=user
                saveform.save()
                
            return redirect('/forex/list')
def forex_delete(request,id):
    if request.user.is_authenticated:
        user = request.user
        forex = forex_details.objects.get(pk=id)
        forex.delete()
        return redirect('/forex/list')

@login_required(login_url='login')   
def forex_edit(request,id):
    if request.method == "POST":
        forex = forex_details.objects.get(pk=id)
        form = forex_details_form(request.POST,instance= forex) 
        if form.is_valid():
            form.save()
        return redirect('/forex/list')
    else:
        forex = forex_details.objects.get(pk=id)
        form = forex_details_form(instance=forex)
        return render(request,"forex/forex_edit.html",{'forex':forex})
@login_required(login_url='login')   
def search_forex(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            ticker=request.POST['ticker']
            api_request=requests.get("https://api.twelvedata.com/time_series?symbol="+ticker+"&dp=2&previous_close=true&outputsize=1&interval=1min&apikey=44a7b9d780db42aeb04f68def28749b5")
            try:
                api=json.loads(api_request.content) 
                json.dumps(api)
            except Exception as e:
                api="Error"
            return render(request,'forex/forex_form.html',{'api':api})
        else:
            return render(request,'forex/forex_form.html',{'ticker':""})