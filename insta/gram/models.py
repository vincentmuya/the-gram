from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.user_name

    def save_user(self):
        self.save()

class Post(models.Model):
    user = models.ForeignKey(User)
    post_image = models.ImageField(upload_to="posts/",blank = True, null = True)
    caption = HTMLField()

    @classmethod
    def this_post(cls):
        gram = cls.objects
        return gram
