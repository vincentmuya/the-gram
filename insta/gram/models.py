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

class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = HTMLField()
    image_image = models.ImageField(upload_to="images/",blank = True)
    caption = models.CharField(max_length = 100)
