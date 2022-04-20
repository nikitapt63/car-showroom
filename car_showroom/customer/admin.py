from django.contrib import admin

from .models import Customer, CustomerPurchasedCars


admin.site.register(Customer)
admin.site.register(CustomerPurchasedCars)
