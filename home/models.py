from django.contrib.auth.decorators import user_passes_test
from django.db import models
from user.models import User
# Create your models here.

class Post(models.Model):
    caption                = models.CharField(default='', max_length=200)
    user                   = models.ForeignKey(User, on_delete=models.CASCADE)

class PostContent(models.Model):
    post                   = models.ForeignKey(Post, on_delete=models.CASCADE)
    file                   = models.FileField(upload_to='posts/')

class Friend(models.Model):
    user                   = models.ForeignKey(User, on_delete=models.CASCADE)
    friends                = models.ManyToManyField(User, related_name="friends", blank=True)
