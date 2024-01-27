# myapi/models.py
from django.db import models
from django.contrib.auth.models import User

class YourModel(models.Model):
    name=models.CharField(max_length=50)
    itemname=models.CharField(max_length=50)
    category = models.CharField(max_length=255)
    image_field = models.ImageField(upload_to='images/')
    description=models.CharField(max_length=200)
