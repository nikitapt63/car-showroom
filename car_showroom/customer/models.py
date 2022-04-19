from django.db import models

from users.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    balance = models.FloatField(verbose_name='Balance', editable=False)

    def __str__(self):
        return f'{self.user}, {self.last_name}, {self.balance}'
