from .models import *
from django import forms

class PostForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    caption = forms.CharField(max_length=200)