from django.shortcuts import get_object_or_404, render,redirect
from .models import mutualfunds_details
from .forms import mutualfunds_details_form
import json,requests
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def mutualfunds_list(request):
    if request.user.is_authenticated:
        user = request.user
        context={'mutualfunds_list':mutualfunds_details.objects.filter(user=user),
        'total_investment':mutualfunds_details.objects.filter(user=user).aggregate(Sum('current_value')),
        'Overall_Gain': mutualfunds_details.objects.filter(user=user).aggregate(Sum('Overall_Gain'))}
        #context={'mutualfunds_list':mutualfunds_details.objects.all()}
        return render(request,"mutualfunds/mutualfunds_list.html",context)
@login_required(login_url='login')
def mutualfunds_form(request,id=0):
        user = request.user
        if request.method == "GET":
            if id == 0:
                form = mutualfunds_details_form()
            else:
                mutualfunds= mutualfunds_details.objects.get(pk=id)
                form = mutualfunds_details_form(instance=mutualfunds)
            return render(request, 'mutualfunds/mutualfunds_form.html', {'form': form})
        else:
            if id == 0:
                form = mutualfunds_details_form(request.POST)
            else:
                mutualfunds = mutualfunds_details.objects.get(pk=id)
                form = mutualfunds_details_form(request.POST,instance=mutualfunds)
            if form.is_valid():
                saveform=form.save(commit=False)
                saveform.user=user
                saveform.save()
                
            return redirect('/mutualfunds/list')


 

def mutualfunds_delete(request,id):
    mutualfunds = mutualfunds_details.objects.get(pk=id)
    mutualfunds.delete()
    return redirect ('/mutualfunds/list')
@login_required(login_url='login')   
def search_mutualfunds(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ticker=request.POST['ticker']
            
            api_request=requests.get("https://financialmodelingprep.com/api/v3/historical-chart/1min/"+ticker+"?apikey=f372ee7729c1db8d2b7d2b908e37842f")
            try:
                api=json.loads(api_request.content) 
            except Exception as e:
                api="Error"
            print(ticker)
            return render(request,'mutualfunds/mutualfunds_form.html',{'api':api[0]})
        else:
            return redirect('/')
@login_required(login_url='login')   
def mutualfunds_edit(request,id):
    if request.method == "POST":
        mutualfunds = mutualfunds_details.objects.get(pk=id)
        form = mutualfunds_details_form(request.POST,instance= mutualfunds) 
        if form.is_valid():
            form.save()
        return redirect('/mutualfunds/list')
    else:
        mutualfunds = mutualfunds_details.objects.get(pk=id)
        form = mutualfunds_details_form(instance=mutualfunds)
        return render(request,"mutualfunds/mutualfunds_edit.html",{'mutualfunds':mutualfunds})