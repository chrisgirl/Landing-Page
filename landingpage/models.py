from django.db import models


# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    content = models.TextField(max_length=1000)