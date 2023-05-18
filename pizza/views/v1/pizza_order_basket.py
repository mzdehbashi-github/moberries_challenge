from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from pizza.models.pizza_order_basket import PizzaOrderBasket
from pizza.serializers.v1.pizza_order_basket import PizzaOrderBasketSerializer


class PizzaOrderBasketView(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = PizzaOrderBasket.objects.select_related('orderresult').prefetch_related('pizzaorderitem_set')
    serializer_class = PizzaOrderBasketSerializer
