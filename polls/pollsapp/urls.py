from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('vote/<int:id>',views.vote,name='vote'),
    path('result/<int:id>',views.result,name='result'),
    path('addque/',views.addque,name='addque'),
    path('addque/addquerecord/',views.addquerecord, name='addquerecord'),
    path('addopt/',views.addopt,name='addopt'),
    path('addopt/addoptrecord/',views.addquerecord, name='addoptrecord')
]
