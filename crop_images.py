from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(default='media/default.jpg', upload_to='profile/picture')

    def __str__(self):
        return f'{self.user.username} Profile'
   
    # This save functions will be provide image crop. how to large image to shart images
     def save(self):
         super().save()

         img = Image.open(self.profile.path)

         if img.height > 300 or img.width > 300:
             output_size = (300, 300)
             img.thumbnail(output_size)
             img.save(self.profile.path)
