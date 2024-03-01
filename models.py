# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Car(models.Model):
#     car_type = models.CharField(max_length=255)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     car_model = models.CharField(max_length=255)
#     renters = models.ManyToManyField(User, through='Rental', related_name='rented_cars')
    
#     def __str__(self):
#         return '{} {}'.format(self.car_type, self.car_model)

# class Rental(models.Model):
#     renter = models.ForeignKey(User, on_delete=models.CASCADE)
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     start_rent = models.DateTimeField()
#     end_rent = models.DateTimeField()
#     how_much = models.IntegerField(default=0)  # Corrected default value

#     def __str__(self):
#         return '{} {}'.format(self.renter, self.car)

        

from django.db import models
from django.contrib.auth import get_user_model

Users = get_user_model()

class Car(models.Model):
    Model = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    Fueltype = models.CharField(max_length=100)
    Dailyrate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return super().__str__()


class Customer(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Contactnumber = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self) -> str:
        return super().__str__()

class Rent(models.Model):
    Rent_Start = models.DateTimeField()
    Rend_End = models.DateTimeField()
    TotalCost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return super().__str__()


class Maintenance(models.Model):
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    Maintenance_date = models.DateTimeField()
    Description = models.TextField()

    def __str__(self) -> str:
        return super().__str__()