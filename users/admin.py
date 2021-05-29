from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# this == admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "birthdate",
                    "currency",
                    "superhost",
                ),
            },
        ),
    )


# class CustomUserAdmin(admin.ModelAdmin):
#     pass


#    list_display = ("username", "gender", "language", "currency", "superhost")
#    list_filter = (
#        "language",
#        "currency",
#        "superhost",
#    )


# this ==> @admin.register(models.User) decorator
# admin.site.register(models.User, CustomUserAdmin)
