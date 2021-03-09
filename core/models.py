from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Snippet(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets')
    code = models.TextField()
    language = models.CharField(max_length=20)
    copies = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.author} | {self.title} | {self.code} | {self.language} | {self.copies}"


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='media', default="media/iconfinder_moon_dark_mode_night_5402400.png")

    def __str__(self):
        return f"{self.user}"

      