from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ADMIN = 1
    USER = 2

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    user = models.OneToOneField(User, related_name="profile",  on_delete=models.CASCADE)


class Album(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Photo(models.Model):
    description = models.CharField(max_length=300)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Bookmark(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
