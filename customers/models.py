from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Customers(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.SET_DEFAULT, default=None)


   
    order = models.CharField(max_length=30, default=None)
    order_history = models.CharField(max_length=30, default=None)
    

    def __str__(self):
        return self.user
