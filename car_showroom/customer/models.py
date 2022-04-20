from django.db import models

from users.models import User
from cars.models import Car


class Customer(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50, verbose_name="Surname")
    balance = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Current balance in $")
    pref_cars = models.JSONField(default={"price": '', "brand": '', "model": '', "fuel_type": '', "year": ''})

    def __str__(self):
        return f'{self.user}, {self.last_name}, {self.balance}'


class CustomerPurchasedCars(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    price = models.FloatField(verbose_name="Purchased price")

    def __str__(self):
        return f'{self.price}'

