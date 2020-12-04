from django.db import models

# Create your models here.
class mostrarPlaylist(models.Model):
    name = models.TextField()
    artist = models.TextField()
    album = models.TextField()
    release = models.DateField()
    duration = models.IntegerField()