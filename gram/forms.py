from django import forms
from django.forms import ModelForm, Textarea
from .models import Post,Profile,Comments,User



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image', 'bio')

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','editor']
        widges = {

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widges = {
        'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }
