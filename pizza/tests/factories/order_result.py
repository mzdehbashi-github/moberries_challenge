import factory

from pizza.models.order_result import OrderResult
from pizza.tests.factories.pizza_order_basket import PizzaOrderBasketFactory


class OrderResultFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = OrderResult

    basket = factory.SubFactory(PizzaOrderBasketFactory)
    status = OrderResult.StatusChoice.DELIVERED
