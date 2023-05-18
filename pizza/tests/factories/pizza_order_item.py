import factory

from pizza.models.pizza_order_item import PizzaOrderItem
from pizza.tests.factories.pizza_order_basket import PizzaOrderBasketFactory
from pizza.tests.factories.pizza import PizzaFactory


class PizzaOrderItemFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PizzaOrderItem

    basket = factory.SubFactory(PizzaOrderBasketFactory)
    pizza = factory.SubFactory(PizzaFactory)
    quantity = 2
