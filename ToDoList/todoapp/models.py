from django.db import models

# Create your models here.
class Task(models.Model):
    tasks = models.CharField(max_length=200)
    duedate = models.DateField(blank=True)

class DoneTask(models.Model):
    donetasks = models.CharField(max_length=200)