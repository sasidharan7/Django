from django.shortcuts import render, redirect
from .models import Profile, Skills, History, HistoryLines, Hobbies
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .forms import sec1form,sec2form

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        userprofile = Profile.objects.filter(owner=request.user)
        userskills = Skills.objects.filter(owner=request.user)
        history = History.objects.filter(owner=request.user).order_by('-enddate')
        historylines = HistoryLines.objects.filter(owner=request.user)
        hobbies = Hobbies.objects.filter(owner=request.user)

        for profile in userprofile:
            form = sec1form(initial={
                'name': profile.name,'email':profile.bioemail,'description':profile.biodescription, 
                'stackoverflow':profile.stackoverflow,
                'linkedin':profile.linkedin,
                'github':profile.github,
                'downloadresume':profile.downloadresume})
        
    return render(request, 'index.html', {'profiles':userprofile, 'form1':form, 'userskills':userskills, 'histories':history,'historylines':historylines, 'hobbies':hobbies})

def section1change(request):
    if request.method == 'POST':
        userprofile = Profile.objects.filter(owner=request.user)
        newname = request.POST.get('name')
        biodescription = request.POST.get('description')
        bioemail = request.POST.get('email')
        stackoverflow = request.POST.get('stackoverflow')
        linkedin = request.POST.get('linkedin')
        github = request.POST.get('github')
        resume = request.POST.get('resume')
        for profile in userprofile:
            profile.name=newname
            profile.biodescription=biodescription
            profile.bioemail=bioemail
            profile.stackoverflow=stackoverflow
            profile.linkedin=linkedin
            profile.github=github
            profile.downloadresume=resume
            profile.save()
    return redirect('index')


def section1_imgchange(request):
    if request.method == 'POST' and "picupload" in request.POST:
        userprofile = Profile.objects.filter(owner=request.user)
        uploadimage = request.FILES.get('dpupload')
        for profile in userprofile:
            profile.emp_image=uploadimage
            profile.save()

    if request.method == 'POST' and "deletepic" in request.POST:
        userprofile = Profile.objects.filter(owner=request.user)
        for profile in userprofile:
            profile.emp_image.delete()

    return redirect('index')


def section2add(request):
    if request.method == 'POST':
        sec2add = request.POST.get('sec2add')
        newskill = Skills(skill=sec2add,owner=request.user)
        newskill.save()
    return redirect('index')

def section2update(request,id):
    if request.method == 'POST' and 'Update/'+id in request.POST:
        skilltext = request.POST.get('text/'+id)
        skillupdate = Skills.objects.get(id=id)
        skillupdate.skill=skilltext
        skillupdate.save()
        return redirect('index')

    if request.method == 'POST' and 'Delete/'+id in request.POST:
        skilltext = request.POST.get('text/'+id)
        skillupdate = Skills.objects.get(id=id)
        skillupdate.delete()
        return redirect('index')

    if request.method == 'POST' and 'Addskill' in request.POST:
        skilltext = request.POST.get('addnewskill')
        newskill = Skills(skill=skilltext,owner=request.user)
        newskill.save()
        return redirect('index')

def section4add(request):
    if request.method == 'POST':
        sec2title = request.POST.get('historytitle')
        sec2company = request.POST.get('historycompany')
        sec2startdate = request.POST.get('historystartdate')
        sec2enddate = request.POST.get('historyenddate')
        sec2desc = request.POST.get('historydesc')
        sec2historyline = request.POST.get('historyachieve')

        sec2history = History(title=sec2title,company=sec2company,startdate=sec2startdate,enddate=sec2enddate,historydesc=sec2desc,owner=request.user)
        sec2history.save()
        sec2achieve = HistoryLines(historyline=sec2historyline,owner=request.user,relhistory=sec2history)
        sec2achieve.save()
    return redirect('index')


def section4update(request,id=None, wh=None):

    try:
        sec4historyline = HistoryLines.objects.get(id=wh)
        sec4historyline.delete()

    except:
        if request.method == 'POST' and 'section4update/'+id in request.POST:
            sec4content = History.objects.get(id=id)
            sec4title = request.POST.get('title/'+id)
            sec4company = request.POST.get('company/'+id)
            sec4startdate = request.POST.get('startdate/'+id)
            sec4enddate = request.POST.get('enddate/'+id)
            sec4desc = request.POST.get('historydesc/'+id)

            sec4historiesrel = HistoryLines.objects.filter(relhistory=sec4content)
            
            
            sec4content.title=sec4title
            sec4content.company=sec4company
            sec4content.startdate=sec4startdate
            sec4content.enddate=sec4enddate
            sec4content.historydesc=sec4desc
            sec4content.owner=request.user
            sec4content.save()

        
            for i in sec4historiesrel:
                j=1
                sec4historyline = request.POST.get('historyline'+str(i.id))
                i.historyline=sec4historyline
                i.owner=request.user
                i.relhistory=sec4content
                i.save()
                j+=1


        if request.method == 'POST' and 'Addachievement/'+id in request.POST:
            sec4content = History.objects.get(id=id)
            achievementtext = request.POST.get('addnewachievement')
            achievementsave = HistoryLines(historyline=achievementtext,owner=request.user,relhistory=sec4content)
            achievementsave.save()

        if request.method == 'POST' and 'section4delete/'+id in request.POST:
            sec4content = History.objects.get(id=id)
            sec4historiesrel = HistoryLines.objects.filter(relhistory=sec4content)
            for i in sec4historiesrel:
                i.delete()        
            sec4content.delete()
    
    

    return redirect('index')

def section5update(request,id=None, hobd=None):
    hobbies = Hobbies.objects.filter(owner=request.user)

    try:
        sec5content = Hobbies.objects.get(id=hobd)       
        sec5content.delete()
    
    except:
        if request.method == 'POST' and 'section5update' in request.POST:
            for i in hobbies:
                sec5hobbyline = request.POST.get('hobby'+str(i.id))
                i.hobby=sec5hobbyline
                i.owner=request.user
                i.save()

        if request.method == 'POST' and 'addhobbybutton' in request.POST:
            newhobby = request.POST.get('addnewhobby')
            newhobbysave = Hobbies(hobby=newhobby,owner=request.user)
            newhobbysave.save()

    return redirect('index')


  
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('login')
    return render(request, 'register.html', {'form':form})


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else: 
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password)

            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Credentials incorrect")
        return render(request, 'login.html', {})


def index_preview(request):
    userprofile = Profile.objects.filter(owner=request.user)
    for profile in userprofile:
        form = sec1form(initial={'name': profile.name,'email':profile.bioemail,'description':profile.biodescription, 'profile_image':profile.emp_image.url})

    return render(request, 'index_preview.html', {'profiles':userprofile, 'form1':form})