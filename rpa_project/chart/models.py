from django.db import models


# Create your models here.
class Top(models.Model):
    rankp = models.IntegerField(primary_key=True)
    song = models.CharField(max_length=200)
    singer = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    likem = models.IntegerField()


class Nation(models.Model):
    rankp = models.IntegerField(primary_key=True)
    song = models.CharField(max_length=200)
    singer = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    likem = models.IntegerField()


class Sea(models.Model):
    rankp = models.IntegerField(primary_key=True)
    song = models.CharField(max_length=200)
    singer = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    likem = models.IntegerField()
