from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, userID, passwork, **kwargs):
        if not userID:
            raise ValueError("userID is required")
        