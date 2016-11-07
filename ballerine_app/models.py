from django.db import models

# Create your models here.

from django.utils.text import slugify

from DancerPortfolio import settings


class StaticText(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title




