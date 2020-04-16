from django.contrib.auth.models import User as u
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserRegistrationForm
from .models import UserFollowing
from post.models import Post


def userr(request):
    return render(request, 'samplelogin/home.html')


def register(request):
    if request.method == 'POST':
        forms = UserRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
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
    context = {
        "user": user1,
        "post": post,
    }
    return render(request, 'samplelogin/userpage.html', context)


def followerhandler(request, user_id):
    follower = request.user
    user1 = u.objects.get(id=user_id)
    UserFollowing.objects.create(user_id=user1.id,
                                 following_user_id=request.user.id)
    url = reverse("userhome", kwargs={"user_id": user_id})
    return HttpResponseRedirect(url)
