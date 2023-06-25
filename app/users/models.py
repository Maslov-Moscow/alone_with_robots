from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from users.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField("email", unique=True)
    first_name = models.CharField("name", max_length=30, blank=True)
    last_name = models.CharField("surname", max_length=30, blank=True)
    date_joined = models.DateTimeField("registered", auto_now_add=True)
    is_active = models.BooleanField("is_active", default=True)
    groups = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
