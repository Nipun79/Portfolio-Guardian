from django.urls import path 
from django.contrib import admin 
from . import views

from django.contrib.auth.views import LogoutView
urlpatterns =[

path('', views.indices_form,name='indices_insert'), 
 path('indices_edit/<int:id>/', views.indices_edit,name='indices_edit'),
path('list/',views.indices_list,name='indices_list'),
path('delete/<int:id>/',views.indices_delete,name='indices_delete'),
path('search_indices/',views.search_indices,name="search_indices")
]
