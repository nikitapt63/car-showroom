from django.db import models

from users.models import User
from cars.models import Car


class Customer(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50, verbose_name="Surname")
    balance = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Current balance in $")

    def __str__(self):
        return f'{self.user}, {self.last_name}, {self.balance}'
