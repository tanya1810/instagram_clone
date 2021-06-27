from home.models import PostContent
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(PostContent)
admin.site.register(Friend)
