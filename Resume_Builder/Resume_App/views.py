from django.shortcuts import render, redirect
from .models import Profile
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .forms import sec1form

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        userprofile = Profile.objects.filter(owner=request.user)
        for profile in userprofile:
            form = sec1form(initial={'name': profile.name,'email':profile.bioemail,'description':profile.biodescription, 'profile_image':''})

    return render(request, 'index.html', {'profiles':userprofile, 'form1':form})

def section1change(request):
    if request.method == 'POST':
        userprofile = Profile.objects.filter(owner=request.user)
        newname = request.POST.get('name')
        biodescription = request.POST.get('description')
        bioemail = request.POST.get('email')
        uploadimage = request.FILES.get('profile_image')
        for profile in userprofile:
            profile.name=newname
            profile.biodescription=biodescription
            profile.bioemail=bioemail
            profile.save()
    return redirect('index')



def section1_imgchange(request):
    if request.method == 'POST':
        userprofile = Profile.objects.filter(owner=request.user)
        uploadimage = request.FILES.get('dpupload')
        for profile in userprofile:
            profile.emp_image=uploadimage
            profile.save()
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