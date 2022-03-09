from django.db import models


# Create your models here.
class event(models.Model):
    name=models.CharField(max_length=50)
    decs=models.TextField(null=True)
    day=models.PositiveIntegerField()
    month=models.PositiveIntegerField()
    year=models.CharField(max_length=4)
    venue=models.CharField(max_length=50)
    time=models.CharField(max_length=10)
    date=models.DateField()
    weblink=models.CharField(max_length=100)
