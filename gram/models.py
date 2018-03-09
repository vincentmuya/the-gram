from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save

# Create your models here.
class Editor(models.Model):
    user_name = models.CharField(User,max_length = 30)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to="posts/",blank = True, null = True)
    bio = models.CharField(max_length = 50, null = True)
    editor = models.ForeignKey(User,null = True)

    def __str__(self):
        return self.user_name

    def save_editor(self):
        self.save()

    @classmethod
    def this_editor(cls):
        gram = cls.objects.all()
        return gram
class Comments(models.Model):
    comment = models.CharField(max_length = 500)
    user = models.ForeignKey(User)



class Post(models.Model):
    editor = models.ForeignKey(User,null = True)
    post_image = models.ImageField(upload_to="posts/",blank = True, null = True)
    caption = HTMLField()

    @classmethod
    def this_post(cls):
        gram = cls.objects.all()
        return gram

def Create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(Create_profile,sender=User)
