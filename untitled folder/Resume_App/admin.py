from django.contrib import admin
from .models import Profile, Skills, History, HistoryLines, Hobbies

# Register your models here.
admin.site.register(Profile)
admin.site.register(Skills)
admin.site.register(History)
admin.site.register(HistoryLines)
admin.site.register(Hobbies)