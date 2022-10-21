from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    tasks = models.CharField(max_length=200)
    duedate = models.DateField(blank=True)
    owner = models.ForeignKey(User, null = True, on_delete=models.CASCADE)

   
class DoneTask(models.Model):
    donetasks = models.CharField(max_length=200)
    owner_donetasks = models.ForeignKey(User, null = True, on_delete=models.CASCADE)