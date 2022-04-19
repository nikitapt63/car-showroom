from django.db import models
from django_countries.fields import CountryField

from users.models import User


class Dealership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = CountryField(blank_label='(select country)', multiple=True)
    balance = models.FloatField(verbose_name='Balance', editable=False)

    def __str__(self):
        return f'{self.user}, {self.location}, {self.balance}'
