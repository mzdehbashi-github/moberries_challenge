from django.db import models


class PizzaOrderItem(models.Model):
    pizza = models.ForeignKey('pizza.Pizza', on_delete=models.RESTRICT)
    basket = models.ForeignKey('pizza.PizzaOrderBasket', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('pizza', 'basket')]
