from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """review admin definition"""

    list_display = ("__str__", "rating_average")
