from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    followers = models.ManyToManyField('self', related_name='follower', blank=True)
    following = models.ManyToManyField('self', related_name='following', blank=True)
    name=models.CharField(max_length=200)
class UserFollowing(models.Model):
    user_id = models.ForeignKey("User", related_name="follow", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey("User", related_name="foll", on_delete=models.CASCADE)
