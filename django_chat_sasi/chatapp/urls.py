from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('checkview',views.checkview,name='checkview'),
    path('messageroom/<str:room_name>/<str:username>',views.messageroom,name='messageroom'),
]
