from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Work(models.Model):
    sno=models.AutoField(primary_key=True)
    email=models.CharField(max_length=100, null=True)
    title=models.CharField(max_length=500, null=True)
    description=models.CharField(max_length=10000, null=True)
    color=models.CharField(max_length=50, null=True)
    complite=models.CharField(max_length=10, null=True)