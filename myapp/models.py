from django.db import models


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=128, default="none")
    author = models.CharField(max_length=128, default="none")
    album = models.CharField(max_length=128, default="none")
    duration = models.CharField(max_length=128, default="none")

    def __str__(self):
        return self.name + " - " + self.author


class User(models.Model):
    userName = models.CharField(max_length=128, default="none")
    email = models.CharField(max_length=128, default="none")

    def __str__(self):
        return self.userName + " - " + self.email


class CollaborativeList(models.Model):
    name = models.CharField(max_length=128, default="none")
    songs = models.ManyToManyField(Song)
    users = models.ManyToManyField(User)
