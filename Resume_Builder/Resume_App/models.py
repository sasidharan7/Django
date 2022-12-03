from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50, null = True, blank = True)
    emp_image = models.ImageField(upload_to='upload/', blank = True, null=True)
    biodescription = models.CharField(max_length=1000, null = True, blank = True)
    bioemail = models.CharField(max_length=100, null = True, blank = True)
    owner = models.ForeignKey(User, null = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name