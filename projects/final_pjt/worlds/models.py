from django.db import models
from django.conf import settings

# Create your models here.
class Profile_icon(models.Model):
    name = models.CharField(max_length=50)
    img_path = models.TextField()
    price = models.IntegerField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='icons')


class Battlelog(models.Model):
    log = models.CharField(max_length=10)
    enermy_id = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Card(models.Model):
    # cardname = models.CharField(max_length=20)
    isnormal = models.BooleanField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    life = models.IntegerField()
    img_url = models.TextField()


class Rankcomment(models.Model):
    content = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)