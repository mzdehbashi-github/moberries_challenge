from decimal import Decimal

import factory

from pizza.models.pizza import Pizza
from pizza.tests.factories.pizza_flavour import PizzaFlavourFactory
from pizza.tests.factories.pizza_size import PizzaSizeFactory


class PizzaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Pizza

    size = factory.SubFactory(PizzaSizeFactory)
    flavour = factory.SubFactory(PizzaFlavourFactory)
    price = Decimal('4.99')
