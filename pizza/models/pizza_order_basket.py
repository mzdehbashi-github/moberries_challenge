from django.db import models


class PizzaOrderBasket(models.Model):
    customer = models.ForeignKey('pizza.Customer', on_delete=models.RESTRICT)
    pizzas = models.ManyToManyField('pizza.Pizza', through='pizza.PizzaOrderItem')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def result(self):
        return getattr(self, 'orderresult', None)

    @property
    def pizzas_count(self):
        value = getattr(self, '_pizzas_count', None)
        if not value:
            value = self.pizzas.all().count()
        return value

    @property
    def items(self):
        return self.pizzaorderitem_set.all()
