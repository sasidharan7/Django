
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register', views.register, name='register'),
    path('login',views.login, name='login'),
    path('section1change/',views.section1change),
    path('section1_imgchange/',views.section1_imgchange),
    path('section2add/',views.section2add),
    path('section2update/<str:id>',views.section2update,name='id'),
    path('section4add/',views.section4add),
    path('section4update/<str:id>',views.section4update,name='id'),
    path('section4deletewh/<str:wh>',views.section4update,name='hl'),
    path('section5deletehobd/<str:hobd>',views.section5update,name='hob'),
    path('section5update/',views.section5update,name='sec5update'),
    path('preview', views.index_preview,name='index_preview'),
]

