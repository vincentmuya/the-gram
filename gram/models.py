from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to="posts/",blank = True, null = True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    @classmethod
    def this_profile(cls):
        gram = cls.objects.all()
        return gram
class Comments(models.Model):
    comment = models.CharField(max_length = 500)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save

    @classmethod
    def this_comment(cls):
        comment = cls.objects.all()
        return comment


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
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
