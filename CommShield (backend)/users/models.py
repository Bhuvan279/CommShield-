from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=200,null=True)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.user

class Missing(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    height = models.CharField(max_length=20)
    last_seen_address = models.CharField(max_length=40)
    last_seen_zip_code = models.CharField(max_length=8)
    desc = models.TextField(max_length=100, null=True)
    
    def __str__(self):
        return self.name
    


    