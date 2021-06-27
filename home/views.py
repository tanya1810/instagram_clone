from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from user.models import *

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        print("post done#############")
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print("Valid done#############")
            images = request.FILES.getlist('file')
            print(images)
            caption= request.POST.get("caption")
            i = Post(caption = caption, user = request.user)
            i.save()
            for image in images:
                new = PostContent(post=i, file = image)
                new.save()
    
    form = PostForm()

    context = {
        'form' : form,
    }
    return render(request, 'home/main.html', context=context)

