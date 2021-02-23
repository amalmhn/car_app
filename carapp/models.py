from django.db import models

# Create your models here.

class Car(models.Model):
    car_name = models.CharField(max_length=250,unique=True)
    mileage = models.IntegerField()
    price = models.IntegerField(default=1.0)
    company = models.CharField(max_length=250)

    def __str__(self):
        return self.car_name