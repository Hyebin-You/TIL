from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    point = models.IntegerField(default=50000)
    tier = models.CharField(max_length=20, default='Bronze')
    win_point = models.IntegerField(default=0)
    nickname = models.CharField(max_length=8)
    blackcube = models.IntegerField(default=0)
    redcube = models.IntegerField(default=0)
    user_icon = models.CharField(max_length=30, default="icon/people.png")


class Usercard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cardname = models.CharField(max_length=20)
    isnormal = models.BooleanField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    life = models.IntegerField()
    img_url = models.CharField(max_length=40)
    ability1 = models.CharField(max_length=10)
    ability2 = models.CharField(max_length=10)
    ability3 = models.CharField(max_length=10)
    ability_grade = models.CharField(max_length=20)


class Attacklist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card1 = models.ForeignKey(Usercard, on_delete=models.CASCADE, null=True, related_name='a_usercards1')
    card2 = models.ForeignKey(Usercard, on_delete=models.CASCADE, null=True, related_name='a_usercards2')
    card3 = models.ForeignKey(Usercard, on_delete=models.CASCADE, null=True, related_name='a_usercards3')


class Defenselist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card1 = models.ForeignKey(Usercard, on_delete=models.CASCADE, null=True, related_name='d_usercards1')
    card2 = models.ForeignKey(Usercard, on_delete=models.CASCADE, null=True, related_name='d_usercards2')
    card3 = models.ForeignKey(Usercard, on_delete=models.CASCADE, null=True, related_name='d_usercards3')