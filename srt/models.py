from django.db import models

# Create your models here.

class Subtitles(models.Model):
    av_name = models.CharField(max_length=80)
    timerange = models.CharField(max_length=100)
    subtitles = models.CharField(max_length=200)
