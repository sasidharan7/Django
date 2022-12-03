
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register', views.register, name='register'),
    path('login',views.login, name='login'),
    path('section1change/',views.section1change),
    path('section1_imgchange/',views.section1_imgchange),
    path('preview', views.index_preview,name='index_preview'),
]

