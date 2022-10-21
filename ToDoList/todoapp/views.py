from django.shortcuts import render, redirect
from .models import Task, DoneTask
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *

@login_required(login_url='login')
def index(request):
    if request.method == "POST" and 'Update' in request.POST:
        task_id = request.POST.get('task_id')
        task=Task.objects.get(id=task_id)
        datepick = request.POST.get('datepick')
        task.duedate = datepick
        task.save()
        
    if request.method == "POST" and 'Completed' in request.POST:
        task_id = request.POST.get('task_id')
        completedtask = Task.objects.get(id=task_id)
        m = DoneTask(donetasks=completedtask.tasks, owner_donetasks=request.user)
        m.save()
        completedtask.delete()

    tasklist = Task.objects.filter(owner=request.user)
    donetasklist = DoneTask.objects.filter(owner_donetasks=request.user)
    return render(request, 'index.html', {'tasklist':tasklist,'donetasklist':donetasklist})


def addtask(request):
    if request.method == "POST":
        x = request.POST.get('task_name')
        y = request.POST.get('newdate')
        z= request.user
        task = Task(tasks=x,duedate=y,owner=z)
        task.save()
        return HttpResponseRedirect(reverse('index'))

def clear_donetasks(request):
    if request.method == "POST":
        donetask_id = request.POST.get('donetask_id')
        cleartask = DoneTask.objects.get(id=donetask_id)
        cleartask.delete()
        return HttpResponseRedirect(reverse('index'))

def clearall_donetasks(request):
    if request.method == "POST" and 'allclear' in request.POST:
        DoneTask.objects.all().delete()
        return HttpResponseRedirect(reverse('index'))

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Credentials incorrect")
        return render(request, 'loginpage.html', {})


def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Account was created")
                return redirect('login')
    return render(request, 'register.html', {'form':form})
    

