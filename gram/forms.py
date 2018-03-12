from django import forms
from django.forms import ModelForm, Textarea
from .models import Post,Editor,Comments

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widges = {
        'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }
