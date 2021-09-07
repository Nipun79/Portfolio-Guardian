# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm,LoginForm
from .models import Account

class CustomUserAdmin(UserAdmin):

    list_display = ['email','first_name','last_name']
    search_fields = ['email']


admin.site.register(Account, CustomUserAdmin)
