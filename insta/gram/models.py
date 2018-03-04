from django.db import models
from django.contrib.auth.models import  User
from tinymce.models import HTMLField
# Create your models here.
class Editor(models.Model):
    user_name = models.CharField(max_length = 30)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to="posts/",blank = True, null = True)

    def __str__(self):
        return self.user_name

    def save_editor(self):
        self.save()

class Post(models.Model):
    editor = models.ForeignKey(Editor,null = True)
    post_image = models.ImageField(upload_to="posts/",blank = True, null = True)
    caption = models.CharField(max_length = 100)

    @classmethod
    def this_post(cls):
        gram = cls.objects.all()
        return gram
