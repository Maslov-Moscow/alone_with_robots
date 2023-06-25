from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.models import User

admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_superuser",
        "last_login",
    )
    ordering = ("id",)
    fields = (
        "first_name",
        "last_name",
        "is_active",
    )
    list_filter = (
        "is_active",
        "is_superuser",
    )
    filter_horizontal = ()
    fieldsets = None
