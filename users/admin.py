from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UsernameField
from . import models
from rooms import models as room_models

# this == admin.site.register(models.User, CustomUserAdmin)


# StackedInline
class RoomInline(admin.TabularInline):

    model = room_models.Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    #    inlines = (RoomInline,)

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
    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
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
