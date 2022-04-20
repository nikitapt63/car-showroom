from django.contrib import admin

from .models import Supplier, SupplierSoldCars


admin.site.register(Supplier)
admin.site.register(SupplierSoldCars)