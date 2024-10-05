from django.db import models

# Create your models here.
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

class Property(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICE , max_length=50)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to="imagehotel/")
    address = models.CharField(max_length=50)
    area = models.IntegerField()
    bed = models.IntegerField()
    bath = models.IntegerField()