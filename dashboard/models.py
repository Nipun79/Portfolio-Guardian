from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Account(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
