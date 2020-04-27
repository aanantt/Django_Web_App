from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class PostComment(models.Model):
    content = models.TextField()
    user = models.ManyToManyField(User)
    date_comment = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        u = User.objects.get(id=self.user)
        return u.username()


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    post_image = models.ImageField(upload_to='postimages/', max_length=200,default="postimages/avatar.png")
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes', blank=True)
    comments = models.ManyToManyField(PostComment, related_name='comments', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
