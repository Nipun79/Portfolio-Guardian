from django.urls import path 
from . import views
from dashboard.views import LoginView, RegisterView

urlpatterns =[
path('',views.home,name="home"),
path('analytics/',views.analytics,name="analytics"),
path('login/' ,LoginView.as_view() , name='login'), 
path('register/' , views.RegisterView.as_view() ,name="register"), 
path('logout/' , views.signout,name='logout' ), 
] 