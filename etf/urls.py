from django.urls import path 
from django.contrib import admin 
from . import views

from django.contrib.auth.views import LogoutView
urlpatterns =[

path('', views.etf_form,name='etf_insert'), 
path('<int:id>/', views.etf_edit,name='etf_edit'),
path('list/',views.etf_list,name='etf_list'),
path('delete/<int:id>/',views.etf_delete,name='etf_delete'),
path('search_etf/',views.search_etf,name="search_etf")
]
