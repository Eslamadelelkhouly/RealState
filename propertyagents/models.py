from django.db import models

# Create your models here.

class PropertyAgents(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='agentsperson/')
    facebooklink = models.URLField(max_length=200)
    instagramlink = models.URLField(max_length=200)
    twittlink = models.URLField(max_length=200)