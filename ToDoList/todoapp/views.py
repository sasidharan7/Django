from random import choices
from django.shortcuts import render
from .models import Task, DoneTask
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime

# Create your views here.
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
        m = DoneTask(donetasks=completedtask.tasks)
        m.save()
        completedtask.delete()


    # if request.method == "POST" and 'Completed' in request.POST:
    #     task_id = request.POST.get('task_id')
    #     task = Task.objects.get(id=task_id)
    #     task.delete()
    tasklist = Task.objects.all()
    donetasklist = DoneTask.objects.all()
    return render(request, 'index.html', {'tasklist':tasklist,'donetasklist':donetasklist})


def addtask(request):
    if request.method == "POST":
        x = request.POST.get('task_name')
        y = request.POST.get('newdate')
        task = Task(tasks=x,duedate=y)
        task.save()
        return HttpResponseRedirect(reverse('index'))

def clear_donetasks(request):
    if request.method == "POST":
        donetask_id = request.POST.get('donetask_id')
        cleartask = DoneTask.objects.get(id=donetask_id)
        cleartask.delete()
        return HttpResponseRedirect(reverse('index'))
