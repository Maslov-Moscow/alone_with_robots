from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from users.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField("Email", unique=True)
    username = models.CharField("Username", max_length=50)
    date_joined = models.DateTimeField("Registered", auto_now_add=True)
    is_active = models.BooleanField("Is_active", default=True)
    groups = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
