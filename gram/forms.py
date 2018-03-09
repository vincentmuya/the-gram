from django import forms
from .models import Post,Editor

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','editor']
        widges = {

        }

class EditprofileForms(forms.ModelForm):
    class Meta:
        model = Editor
        exclude = ['editor']
        widges = {

        }
