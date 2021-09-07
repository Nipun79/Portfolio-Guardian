from django.urls import path 
from django.contrib import admin 
from . import views

from django.contrib.auth.views import LogoutView
urlpatterns =[

path('', views.crypto_form,name='crypto_insert'), 
path('<int:id>/', views.crypto_edit,name='crypto_edit'),
path('list/',views.crypto_list,name='crypto_list'),
path('delete/<int:id>/',views.crypto_delete,name='crypto_delete'),
path('search_crypto/',views.search_crypto,name="search_crypto")
]
