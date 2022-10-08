from random import choices
from django.shortcuts import render
from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'index.html', {'questions':questions})

def vote(request,id):
    question = Question.objects.get(id=id)
    options = question.choices.all()
    return render(request, 'vote.html', {'question':question,'options':options})

def result(request, id):
    question = Question.objects.get(id=id)
    options = question.choices.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 5
        selection_option.save()

    return render(request, 'result.html', {'question':question,'options':options})

def addque(request):
    return render(request, 'addque.html', {})

def addquerecord(request):
    que = request.POST.get('que')
    pollque = Question(question=que)
    pollque.save()
    return HttpResponseRedirect(reverse('index'))

def addopt(request):
    questions = Question.objects.all()
    return render(request, 'addopt.html', {'questions':questions})

def addoptrecord(request):
    ch = request.POST.get('ch')
    vo = request.POST.get('vo')
    optquestions = request.POST.get('optquestions')
    que = Question.objects.get(id=optquestions)

    pollopt = Choice(question = que,option=ch,vote=vo)
    pollopt.save()
    return HttpResponseRedirect(reverse('index'))