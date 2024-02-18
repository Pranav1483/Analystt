from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=500)

class Task(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    deadline = models.DateTimeField()