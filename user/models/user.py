from datetime import date

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from ..managers import UserManager
from ..user_utility import UserGender


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(default='2025-02-04', blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    city = models.CharField(max_length=11, blank=True)
    user_gender = models.CharField(max_length=1, choices=UserGender.choices)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_confirmed_email = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    objects = UserManager()

    def __str__(self):
        return self.email
