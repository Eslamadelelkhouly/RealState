from django.db import models

# Create your models here.

class Contact(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    facebooklink = models.URLField(max_length=200)
    instagramlink = models.URLField(max_length=200)
    yotubelink = models.URLField(max_length=200)
    linkedlnlink = models.URLField(max_length=200)