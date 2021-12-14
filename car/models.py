from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Register(models.Model):
    Name = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    Mobile = models.CharField(max_length=250)
    Gender = models.CharField(max_length=250)
    City = models.CharField(max_length=250)
    Password = models.CharField(max_length=250)

