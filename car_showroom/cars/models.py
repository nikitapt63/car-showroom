import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


now = datetime.datetime.now()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')


class Car(models.Model):
    """Fuel type choices"""
    CHOICES = (
        ('GSL', 'Gasoline'),
        ('DSL', 'Diesel'),
        ('GAS', 'Gas'),
        ('ELC', 'Electric'),
    )
    image = models.OneToOneField(Image, blank=True, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Car's price($)")
    brand = models.CharField(max_length=50, verbose_name="Car's brand")
    model = models.CharField(max_length=50, verbose_name="Car's model")
    fuel_type = models.CharField(max_length=50, choices=CHOICES, verbose_name="Car's fuel type")
    year = models.IntegerField(validators=[MaxValueValidator(now.year)], verbose_name='Year of issue')

    def __str__(self):
        return f'{self.price}, {self.brand}, {self.model}, {self.fuel_type}, {self.year}'


