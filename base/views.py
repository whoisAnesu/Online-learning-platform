from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.decorators import login_required   
from django.db.models import Q 
from .models import Room, Topic, Message   
from .forms import RoomForm 
from django.contrib.auth.models import User 
from mychatapp.models import Profile, Friend


def rooms_home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains= q) | 
                                Q(name__icontains=q) |
                                Q(description__icontains=q))
    
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.all().filter(Q(room__name__icontains=q))
    
    context = {'rooms': rooms, 'topics': topics, 
            'room_count':room_count, 'room_messages': room_messages}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    roommessages = room.message_set.all()
    participants = room.participants.all()
    
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user, 
            room=room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    
    context = {'room': room, 'roommessages': roommessages,
            'participants': participants}
    return render(request, 'base/room.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(id=pk)
    firstName = user.first_name
    lastName = user.last_name
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 
            'room_messages': room_messages, 'topics': topics,
            'firstName': firstName, 'lastName': lastName, 'profile': profile}
    return render(request, 'base/profile.html', context)

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('rooms_home')
    
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed in here')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms_home')
    
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed in here')
    
    if request.method == "POST":
        room.delete()
        return redirect('rooms_home')
    return render(request, 'base/delete.html', {'obj': room}) 


@login_required(login_url='/login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse('You are not allowed in here')
    
    if request.method == "POST":
        message.delete()
        return redirect('rooms_home')
    return render(request, 'base/delete.html', {'obj': message})