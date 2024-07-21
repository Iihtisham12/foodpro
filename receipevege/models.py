from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank=True)
    re_name = models.CharField(max_length=100)
    re_description = models.TextField(max_length=1000)
    re_price = models.IntegerField()
    re_images = models.ImageField(upload_to='receipe')