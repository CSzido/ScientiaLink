from django.shortcuts import render, redirect
from .forms import SignUP
from django.contrib.auth import authenticate, login
from Main.models import *
from.models import *
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        Form = SignUP(request.POST)
        if Form.is_valid() and request.FILES["image"] != "":
            Form.save()
            username = Form.cleaned_data['username']
            password = Form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            interest = Interest.objects.get(interest=request.POST["interest0"])
            request.user.profile.interests.add(interest)
            if request.POST["interest1"] != "":
                interest1 = Interest.objects.get(interest=request.POST["interest1"])
                request.user.profile.interests.add(interest1)
            if request.POST["interest2"] != "":
                interest2 = Interest.objects.get(interest=request.POST["interest2"])
                request.user.profile.interests.add(interest2)
            image = request.FILES["image"]
            full_name = request.POST["name"]
            request.user.profile.image = image
            request.user.profile.full_name = full_name
            request.user.profile.save()
            return redirect(f'/')
    else:
        Form = SignUP()
    return render(request, 'registration/sign_up.html', {'Form': Form})


def follow(request, id):
    user = request.user.profile
    friend = profile.objects.get(id=id)
    if user not in friend.followers.all():
        user.following.add(friend)
        friend.followers.add(user)
    else:
        user.following.remove(friend)
        friend.followers.remove(user)
    return redirect("/")
# Create your views here.
