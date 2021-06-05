from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    review = models.TextField()
