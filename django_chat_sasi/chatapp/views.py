from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def checkview(request):
    room_name=request.POST.get('room_name')
    username = request.POST.get('username')
    Roomexists = Room.objects.filter(roomname=room_name)

    if Roomexists.exists():
        return redirect('messageroom/'+room_name+'/'+username) 

    else: 
        newroom = Room(roomname=room_name)
        newroom.save()
        return redirect('messageroom/'+room_name+'/'+username)

def messageroom(request,room_name,username):
    if request.method == "POST":
        messagetext = request.POST.get('message')
        newmessage = Message(messagetext=messagetext,messageroom=room_name,username=username)
        newmessage.save()
    
    listmessages = Message.objects.filter(messageroom=room_name)
    return render(request, 'room.html', {'listmessages':listmessages,'room_name':room_name,'username':username})
   


