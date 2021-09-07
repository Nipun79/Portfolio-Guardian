from django.urls import path 
from django.contrib import admin 
from . import views

from django.contrib.auth.views import LogoutView
urlpatterns =[

path('', views.stock_form,name='stock_insert'), 
 path('stock_edit/<int:id>/', views.stock_edit,name='stock_edit'),
path('list/',views.stock_list,name='stock_list'),
path('delete/<int:id>/',views.stock_delete,name='stock_delete'),
path('search_stock/',views.search_stock,name="search_stock")
]
