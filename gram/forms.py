from django import forms
from .models import Post,Editor

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
        widges = {

        }

class Editprofile(forms.ModelForm):
    class Meta:
        model = Editor
        exclude = []
        widges = {

        }
