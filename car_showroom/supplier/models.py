from django.db import models

from users.models import User


class Supplier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foundation = models.IntegerField(verbose_name='Foundation year')

    def __str__(self):
        return f'{self.user}, {self.foundation}'



