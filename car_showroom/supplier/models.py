from django.db import models

from users.models import User
from cars.models import Car


class Supplier(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foundation = models.IntegerField(verbose_name='Foundation year')

    def __str__(self):
        return f'{self.user}, {self.foundation}'



