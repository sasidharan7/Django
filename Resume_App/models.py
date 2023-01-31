from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50, null = True, blank = True)
    emp_image = models.ImageField(upload_to='upload/', blank = True, null=True)
    biodescription = models.CharField(max_length=1000, null = True, blank = True)
    bioemail = models.CharField(max_length=100, null = True, blank = True)
    owner = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    stackoverflow = models.CharField(max_length=500, null = True, blank = True)
    linkedin = models.CharField(max_length=500, null = True, blank = True)
    github = models.CharField(max_length=500, null = True, blank = True)
    downloadresume = models.CharField(max_length=500, null = True, blank = True)

    def __str__ (self):
        return self.name
    

class Skills(models.Model):
    skill = models.CharField(max_length=500, null = True, blank = True)
    owner = models.ForeignKey(User, null = True, on_delete=models.CASCADE)

class History(models.Model):
    title = models.CharField(max_length=500, null = True, blank = True)
    company = models.CharField(max_length=500, null = True, blank = True)
    startdate = models.DateField()
    enddate = models.DateField()
    historydesc = models.CharField(max_length=500, null = True, blank = True)
    owner = models.ForeignKey(User, null = True, on_delete=models.CASCADE)

    def __str__ (self):
        return self.company

class HistoryLines(models.Model):
    historyline = models.CharField(max_length=5000, null = True, blank = True)
    owner = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    relhistory = models.ForeignKey(History, null = True, on_delete=models.CASCADE)

class Hobbies(models.Model):
    hobby = models.CharField(max_length=5000, null = True, blank = True)
    owner = models.ForeignKey(User, null = True, on_delete=models.CASCADE)

   

    