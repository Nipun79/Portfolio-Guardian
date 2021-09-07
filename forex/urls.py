from django.urls import path 
from django.contrib import admin 
from . import views

from django.contrib.auth.views import LogoutView
urlpatterns =[

path('', views.forex_form,name='forex_insert'), 
path('<int:id>/', views.forex_edit,name='forex_edit'),
path('list/',views.forex_list,name='forex_list'),
path('delete/<int:id>/',views.forex_delete,name='forex_delete'),
path('search_forex/',views.search_forex,name="search_forex")
]
