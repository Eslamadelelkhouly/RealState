from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='bloimage/')
    hotelname = models.CharField(max_length=50)

CATEGORY_CHOICE = (
    ('AT','Apartment'),
    ('VA','Vila'),
    ('HE','Home'),
    ('OE','Office'),
    ('BG','Building'),
    ('TE','Townhouse'),
    ('SP','Shop'),
    ('GE','Grage'),
)

class PropertyType(models.Model):
    name = models.CharField(choices=CATEGORY_CHOICE , max_length=50)
    image = models.ImageField(upload_to='propertytype/')

class Search(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICE , max_length=50)
    address = models.CharField(max_length=50)
