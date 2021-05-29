from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.


class Room(core_models.TimeStampedModel):
    """Room modeling"""

    name = CharField(max_length=140)
    description = models.TextField()
    country = models.CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
