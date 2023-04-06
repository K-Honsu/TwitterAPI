from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone_number, password=None):
        if not email:
            raise ValueError('Please enter valid email')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, phone_number, password=None):
        """
        creates and saves a superuser with the given email, first_name, last_name and password
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            phone_number,
            password=password
        )
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class UserAccount(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name
