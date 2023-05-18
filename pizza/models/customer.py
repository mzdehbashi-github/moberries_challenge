from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
