from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    """ User model: identification by email, additional field: name. """
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=50, verbose_name='name')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField('verified', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return f'{self.email}, {self.name}'


