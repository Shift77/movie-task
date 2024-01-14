from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUSerManager


class User(AbstractBaseUser, PermissionsMixin):
    '''Custom user model wth phone number.'''
    phone_number = models.CharField(max_length=11, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = CustomUSerManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number
