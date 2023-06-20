from django.db import models

# Create your models here.
class Work(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=10000)
    color=models.CharField(max_length=50)
    complite=models.CharField(max_length=10)