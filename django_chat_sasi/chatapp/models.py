from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    roomname = models.CharField(max_length=1000)

class Message(models.Model):
    messagetext = models.CharField(max_length=10000)
    username = models.CharField(max_length=1000)
    datetime = models.DateTimeField(default=datetime.now,blank=True)
    messageroom = models.CharField(max_length=1000)