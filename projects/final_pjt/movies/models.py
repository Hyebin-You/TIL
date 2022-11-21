from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')


class Playlist(models.Model):
    isopened = models.BooleanField(default=False)
    title = models.CharField(max_length=10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField(null=True)
    vote_average = models.FloatField()
    popularity = models.FloatField()
    video_key = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    playlists = models.ManyToManyField(Playlist, related_name='in_movies')


class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=40)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)