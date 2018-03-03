from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.user_name

    def save_user(self):
        self.save()

class Image(models.Model):
    image_image = models.ImageField(upload_to="images/",blanl = True)
    caption = models.CharField()
