from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    """review model definition"""

    review = models.TextField(null=True)
    Accuracy = models.IntegerField(null=True)
    communication = models.IntegerField(null=True)
    cleanliness = models.IntegerField(null=True)
    location = models.IntegerField(null=True)
    check_in = models.IntegerField(null=True)
    value = models.IntegerField(null=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=True, blank=True
    )
    room = models.ForeignKey("rooms.Room", on_delete=CASCADE, null=True, blank=True)
    ### if foreign key, can access
    def __str__(self):
        return f"{self.review} - {self.room}"
