from django.db import models

# Create your models here.

class task(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
    date=models.DateField()
    time=models.TimeField()