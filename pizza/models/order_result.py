from django.db import models


class OrderResult(models.Model):

    class StatusChoice(models.TextChoices):
        DELIVERED = 'delivered'
        CANCELED = 'canceled'

    basket = models.OneToOneField('pizza.PizzaOrderBasket', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=StatusChoice.choices)
