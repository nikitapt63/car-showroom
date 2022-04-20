from django.db import models
from django_countries.fields import CountryField

from users.models import User
from cars.models import Car


class Dealership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    location = CountryField(blank_label='(select country)', multiple=True)
    balance = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Current balance in $")
    pref_cars = models.JSONField(default={"price": '', "brand": '', "model": '', "fuel_type": '', "year": ''})

    def __str__(self):
        return f'{self.user}, {self.location}, {self.balance}'


class DealershipSoldCars(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, null=True)
    price = models.FloatField(verbose_name="Sold price")

    def __str__(self):
        return f'{self.price}'
