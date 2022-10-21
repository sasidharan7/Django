from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('addtask/',views.addtask, name='addtask'),
    path('clear_donetasks/',views.clear_donetasks, name='clear_donetasks'),
    path('clearall_donetasks/',views.clearall_donetasks, name='clearall_donetasks'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutUser,name='logout')
]
