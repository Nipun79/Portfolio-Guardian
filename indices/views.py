from django.shortcuts import get_object_or_404, render,redirect
from .models import indices_details
from .forms import indices_details_form
import json,requests
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def indices_list(request):
    if request.user.is_authenticated:
        user = request.user
        context={'indices_list':indices_details.objects.filter(user=user),
        'total_investment':indices_details.objects.filter(user=user).aggregate(Sum('current_value')),
        'Overall_Gain': indices_details.objects.filter(user=user).aggregate(Sum('Overall_Gain'))}
        #context={'indices_list':indices_details.objects.all()}
        return render(request,"indices/indices_list.html",context)
@login_required(login_url='login')
def indices_form(request,id=0):
        user = request.user
        if request.method == "GET":
            if id == 0:
                form = indices_details_form()
            else:
                indices= indices_details.objects.get(pk=id)
                form = indices_details_form(instance=indices)
            return render(request, 'indices/indices_form.html', {'form': form})
        else:
            if id == 0:
                form = indices_details_form(request.POST)
            else:
                indices = indices_details.objects.get(pk=id)
                form = indices_details_form(request.POST,instance=indices)
            if form.is_valid():
                saveform=form.save(commit=False)
                saveform.user=user
                saveform.save()
                
            return redirect('/indices/list')


 

def indices_delete(request,id):
    indices = indices_details.objects.get(pk=id)
    indices.delete()
    return redirect ('/indices/list')
@login_required(login_url='login')   
def search_indices(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            ticker=request.POST['ticker']
            api_request=requests.get("https://api.twelvedata.com/time_series?symbol="+ticker+"&dp=2&previous_close=true&outputsize=1&interval=1min&apikey=44a7b9d780db42aeb04f68def28749b5")
            try:
                api=json.loads(api_request.content) 
            except Exception as e:
                api="Error"
            return render(request,'indices/indices_form.html',{'api':api})
        else:
            return redirect('/')
@login_required(login_url='login')   
def indices_edit(request,id):
    if request.method == "POST":
        indices = indices_details.objects.get(pk=id)
        form = indices_details_form(request.POST,instance= indices) 
        if form.is_valid():
            form.save()
        return redirect('/indices/list')
    else:
        indices = indices_details.objects.get(pk=id)
        form = indices_details_form(instance=indices)
        return render(request,"indices/indices_edit.html",{'indices':indices})