from django.contrib.auth.decorators import user_passes_test
from django.db import models
from user.models import User
# Create your models here.

class Post(models.Model):
    caption                = models.CharField(default='', max_length=200)
    user                   = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)

class PostContent(models.Model):
    post                   = models.ForeignKey(Post, on_delete=models.CASCADE)
    file                   = models.FileField(upload_to='posts/')
    def __str__(self):
        return str(self.post.user)

