from django.db import models

class Registration(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
