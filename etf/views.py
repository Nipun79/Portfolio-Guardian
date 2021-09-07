from django.shortcuts import render,redirect
from .models import etf_details
from .forms import etf_details_form
import json,requests
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def etf_list(request):
    if request.user.is_authenticated:
        user = request.user
        context={'etf_list':etf_details.objects.filter(user=user),
        'total_investment':etf_details.objects.filter(user=user).aggregate(Sum('current_value')),
        'Overall_Gain': etf_details.objects.filter(user=user).aggregate(Sum('Overall_Gain'))}
        #context={'etf_list':etf_details.objects.all()}
        return render(request,"etf/etf_list.html",context)
@login_required(login_url='login')
def etf_form(request,id=0):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "GET":
            if id == 0:
                form = etf_details_form()
            else:
                etf= etf_details.objects.get(pk=id)
                form = etf_details_form(instance=etf)
            return render(request, 'etf/etf_form.html', {'form': form})
        else:
            if id == 0:
                form = etf_details_form(request.POST)
            else:
                etf = etf_details.objects.get(pk=id)
                form = etf_details_form(request.POST,instance=etf)
            if form.is_valid():
                saveform=form.save(commit=False)
                saveform.user=user
                saveform.save()
                
            return redirect('/etf/list')
def etf_delete(request,id):
    if request.user.is_authenticated:
        user = request.user
        etf = etf_details.objects.get(pk=id)
        etf.delete()
        return redirect('/etf/list')

@login_required(login_url='login')   
def etf_edit(request,id):
    if request.method == "POST":
        etf = etf_details.objects.get(pk=id)
        form = etf_details_form(request.POST,instance= etf) 
        if form.is_valid():
            form.save()
        return redirect('/etf/list')
    else:
        etf = etf_details.objects.get(pk=id)
        form = etf_details_form(instance=etf)
        return render(request,"etf/etf_edit.html",{'etf':etf})
@login_required(login_url='login')   
def search_etf(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            ticker=request.POST['ticker']
            api_request=requests.get("https://api.twelvedata.com/time_series?symbol="+ticker+"&previous_close=true&outputsize=1&interval=1min&apikey=44a7b9d780db42aeb04f68def28749b5")
            try:
                api=json.loads(api_request.content) 
                json.dumps(api)
            except Exception as e:
                api="Error"
            return render(request,'etf/etf_form.html',{'api':api})
        else:
            return render(request,'etf/etf_form.html',{'ticker':""})