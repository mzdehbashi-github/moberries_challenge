import factory

from pizza.models.pizza_order_basket import PizzaOrderBasket
from pizza.tests.factories.customer import CustomerFactory


class PizzaOrderBasketFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PizzaOrderBasket

    customer = factory.SubFactory(CustomerFactory)

