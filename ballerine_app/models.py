from django.db import models

# Create your models here.

from django.utils.text import slugify

from DancerPortfolio import settings


class StaticText(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

class HomeImage(models.Model):
    title = models.CharField(max_length=120)
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title

class MiniGallery(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=120)
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.titled

