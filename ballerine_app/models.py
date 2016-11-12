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
        return self.title


class Social(models.Model):
    title = models.CharField(max_length=20)
    url = models.URLField(default=None)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default=None)
    message = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

