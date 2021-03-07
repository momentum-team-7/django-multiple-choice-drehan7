from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Snippet(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets')
    code = models.TextField()
    language = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.author} | {self.title} | {self.code} | {self.language}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return f"{self.user}"