from django.db import models
from django.contrib.auth.models import AbstractUser

from stock.models import Department

# Create your models here.

class User(AbstractUser):
    role = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='user_dep_name', blank=True, null=True)