from django.shortcuts import get_object_or_404, render,redirect
from .models import Stock_details
from .forms import Stock_details_form
import json,requests
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def stock_list(request):
    if request.user.is_authenticated:
        user = request.user
        context={'stock_list':Stock_details.objects.filter(user=user),
        'total_investment':Stock_details.objects.filter(user=user).aggregate(Sum('current_value')),
        'Today_Gain': Stock_details.objects.filter(user=user).aggregate(Sum('Today_Gain')), 
        'Overall_Gain': Stock_details.objects.filter(user=user).aggregate(Sum('Overall_Gain')),
       
        }
        #context={'stock_list':Stock_details.objects.all()}
        return render(request,"stocks/stock_list.html",context)
@login_required(login_url='login')
def stock_form(request,id=0):
        user = request.user
        if request.method == "GET":
            if id == 0:
                form = Stock_details_form()
            else:
                Stocks= Stock_details.objects.get(pk=id)
                form = Stock_details_form(instance=Stocks)
            return render(request, 'stocks/stock_form.html', {'form': form})
        else:
            if id == 0:
                form = Stock_details_form(request.POST)
            else:
                Stocks = Stock_details.objects.get(pk=id)
                form = Stock_details_form(request.POST,instance=Stocks)
            if form.is_valid():
                saveform=form.save(commit=False)
                saveform.user=user
                saveform.save()
            return redirect('/stocks/list')
def stock_delete(request,id):
    Stocks = Stock_details.objects.get(pk=id)
    Stocks.delete()
    return redirect ('/stocks/list')
@login_required(login_url='login')   
def search_stock(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            ticker=request.POST['ticker']
            api_request=requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_e9d451b418d547cba28926a19e4681f5")
            try:
                api=json.loads(api_request.content) 
            except Exception as e:
                api="Error"
            return render(request,'stocks/stock_form.html',{'api':api})
        else:
            return redirect('/')
@login_required(login_url='login')   
def stock_edit(request,id):
    if request.method == "POST":
        stock = Stock_details.objects.get(pk=id)
        form = Stock_details_form(request.POST,instance= stock) 
        if form.is_valid():
            form.save()
        return redirect('/stocks/list')
    else:
        stock = Stock_details.objects.get(pk=id)
        form = Stock_details_form(instance=stock)
        return render(request,"stocks/stock_edit.html",{'stock':stock})