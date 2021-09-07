from django.urls import path 
from django.contrib import admin 
from . import views

from django.contrib.auth.views import LogoutView
urlpatterns =[

path('', views.mutualfunds_form,name='mutualfunds_insert'), 
 path('mutualfunds_edit/<int:id>/', views.mutualfunds_edit,name='mutualfunds_edit'),
path('list/',views.mutualfunds_list,name='mutualfunds_list'),
path('delete/<int:id>/',views.mutualfunds_delete,name='mutualfunds_delete'),
path('search_mutualfunds/',views.search_mutualfunds,name="search_mutualfunds")
]
