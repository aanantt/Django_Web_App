from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from .models import Post, PostComment


class PostListView(ListView):
    model = Post
    context_object_name = 'post'
    ordering = ['-date_posted']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required
def detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post/post_detail.html", {'object': post})

@login_required
def like_disliked(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    print("Total", post.likes.count())
    url = reverse("post-detail", kwargs={"post_id": post.id})
    return HttpResponseRedirect(url)

@login_required
def load(request, post_id):
    if request.method == "POST":
        if request.POST.get("comment"):
            text = request.POST.get("comment")
            print("text is ", text)
            post = Post.objects.get(id=post_id)
            comment = PostComment.objects.create(content=str(text))
            comment.save()
            comment.user.add(request.user)
            post.comments.add(comment)
    url = reverse("post-detail", kwargs={"post_id": post_id})
    return HttpResponseRedirect(url)

@login_required
def delete_comment(request, pk, c):
    comment = PostComment.objects.get(id=c)
    comment.delete()
    url = reverse("post-detail", kwargs={"post_id": pk})
    return HttpResponseRedirect(url)

@login_required
def search(request):
    if request.method == "POST":
        if request.POST.get("search"):
            print("text GOT")
            data = request.POST.get("search")
            post = Post.objects.filter(title__icontains=data)
            user = User.objects.filter(username__icontains=data)
            context = {
                'post': post,
                'user_list': user,
            }
            return render(request,'post/search.html', context)

