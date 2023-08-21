from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    credit_card_info = models.IntegerField(max_length=16)
    user_name = models.CharField(max_length=100)
