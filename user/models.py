"""
Database models for user.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address')
        if not first_name:
            raise ValueError('User must have a first name')
        if not last_name:
            raise ValueError('User must have a last name')
        user = self.model(
            email=self.normalize_email(email), first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name, last_name):
        """Create and return a new superuser."""
        user = self.create_user(email, password, first_name, last_name)
        user.role = 'ADMINISTRATOR'
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    role = models.CharField(
        max_length=20, choices=(('ADMINISTRATOR', 'Administrator'), ('WORKER', 'Worker')), default='WORKER'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
