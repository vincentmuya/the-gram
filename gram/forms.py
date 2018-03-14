from django import forms
from django.forms import ModelForm, Textarea
from .models import Post,Profile,Comments

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','editor']
        widges = {

        }

class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widges = {

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widges = {
        'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }
