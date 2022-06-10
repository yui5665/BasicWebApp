from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    mail = models.CharField(max_length=128)
    def __str__(self):
        return self.username

class File(models.Model):
    name = models.CharField(max_length=128)
    dimension = models.IntegerField()
    date = models.DateTimeField()
    TYPE = (
        ('Document','Document'),
        ('Image','Image'),
        ('Audio','Audio'),
        ('Video','Video'),
        ('Unknown','Unknown')
    )
    type = models.CharField(
        max_length=8 ,default='Unknown', choices=TYPE
        )
    def __str__(self):
        return self.name

class Authorization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    TYPE = (
        ('None', 'None'),
        ('Read','Read'),
        ('Write', 'Write')
    )
    autorization = models.CharField(
        max_length=128, default='None', choices=TYPE
        )

modelsList = [User, File, Authorization]
