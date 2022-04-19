# Generated by Django 3.2.9 on 2022-04-19 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_create_car_and_image_models'),
        ('dealership', '0001_create_dealership_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealership',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
    ]
