from django.db import models


# Create your models here.
class event(models.Model):
    admin_code=models.CharField(max_length=4)
    name=models.CharField(max_length=50)
    decs=models.CharField(max_length=500)
    day=models.PositiveIntegerField()
    month=models.PositiveIntegerField()
    year=models.CharField(max_length=4)
    venue=models.CharField(max_length=50)
    time=models.CharField(max_length=10)
    date=models.DateField()
    weblink=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    message=models.TextField(null=True)

    def __str__(self):
        return self.name
class comment(models.Model):
    text=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    commentid=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name