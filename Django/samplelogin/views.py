from django.contrib.auth.models import User as u, User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from post.models import Post

from .forms import UserRegistrationForm, UserProfileForm
from .models import UserFollowing, UserProfile


def userr(request):
    user = User.objects.get(id=request.user.id)
    profile = UserProfile.objects.get(user=user)
    post = Post.objects.filter(author=request.user)
    context = {
        'user': user,
        'profile': profile,
        'post': post,
    }
    return render(request, 'samplelogin/userpage.html', context)


def register(request):
    if request.method == 'POST':
        forms = UserRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            user1 = User.objects.get(username=forms.cleaned_data['username'])
            data = UserProfile(user=user1)
            data.save()
            return redirect('home')
        else:
            return HttpResponse("<h1>ERROR</h1>")
    if request.method == 'GET':
        form = UserRegistrationForm()
    return render(request, 'samplelogin/signup.html', {'form': form})


def userhome(request, user_id):
    user1 = u.objects.get(id=user_id)
    current_user = request.user
    post = Post.objects.filter(author=user1)
    profile = UserProfile.objects.filter(user=current_user)
    context = {
        "user": user1,
        "post": post,
        "profile": profile
    }
    return render(request, 'samplelogin/userpage.html', context)


def followerhandler(request, user_id):
    follower = request.user
    user1 = u.objects.get(id=user_id)
    UserFollowing.objects.create(user_id=user1.id,
                                 following_user_id=request.user.id)
    url = reverse("userhome", kwargs={"user_id": user_id})
    return HttpResponseRedirect(url)


def image(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            data = UserProfile(user=request.user, avatar=form.cleaned_data["avatar"])
            data.save()
            return redirect("home")
    elif request.method == "GET":
        form = UserProfileForm()
    return render(request, "samplelogin/image.html", {'form': form})
