from email.policy import default
from turtle import title
from django.db import models
from datetime import datetime


class Artiste(models.Model):
    name = models.CharField(max_length=400)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()

    def __str__(self):
        return self.name


class Lyric(models.Model):
    name = models.CharField(max_length=40)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000000)

    def __str__(self):
        return self.name