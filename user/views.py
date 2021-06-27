from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.http import HttpResponse, request
User = get_user_model()
from home.models import *

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User = form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def findfriends(request):
    u = request.user
    e = u.email
    all_users = User.objects.exclude(friend__email = e)
    # print("####################################")
    # print(all_users)
    # print("####################################")
    context = {
        'all_users' : all_users,
        'user':u
    }
    return render(request,'user/findfriends.html', context=context)

def sendreq(request, pk):
    t = User.objects.filter(id = pk).first()
    # print(FriendRequest.objects.filter(from_user = request.user).filter(to_user = t))
    if FriendRequest.objects.filter(from_user = request.user).filter(to_user = t):
        pass
    else:
        new = FriendRequest(from_user = request.user, to_user = t)
        new.save()
    return redirect('findfriends')

def myprofile(request):
    req = FriendRequest.objects.filter(to_user = request.user).filter(is_accepted = False)
    return render(request, 'user/myprofile.html', {'req' : req})

def acceptreq(request, pk):
    obj = FriendRequest.objects.filter(id=pk).first()
    obj.is_accepted = True
    obj.save()
    f = obj.from_user
    t = obj.to_user
    u = User.objects.filter(id = f.id).first()
    # print(u.friend)
    u.friend.add(t)
    u = User.objects.filter(id = t.id).first()
    # print(u.friend)
    u.friend.add(f)
    return redirect('myprofile')

