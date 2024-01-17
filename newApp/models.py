from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# This one is a simple model, for a regular Login page
class AppUsers(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=200, blank=False)
    bio = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# This one is a special User Class, that has one-to-one relation with Django Users Model
class UserExtension(models.Model):

    # Creating Django User relation for this extension class
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Creating extra fields
    links = models.URLField(max_length=200, unique=False, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username
