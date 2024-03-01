from django.contrib import admin
from .models import Car, Customer, Rent, Maintenance

# Register your models here.
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Rent)
admin.site.register(Maintenance)


