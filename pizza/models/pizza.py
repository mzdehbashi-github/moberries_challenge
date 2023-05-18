from django.db import models


class Pizza(models.Model):
    flavour = models.ForeignKey('pizza.PizzaFlavour', on_delete=models.RESTRICT)
    size = models.ForeignKey('pizza.PizzaSize', on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = [('flavour', 'size')]

    def __str__(self):
        return f'{self.flavour.name}:{self.size.name}:{self.price}'
