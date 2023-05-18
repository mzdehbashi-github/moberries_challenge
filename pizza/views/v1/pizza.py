from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from pizza.models.pizza import Pizza
from pizza.serializers.v1.pizza import PizzaSerializer


class PizzaView(GenericViewSet, mixins.ListModelMixin):
    queryset = Pizza.objects.select_related('size', 'flavour')
    serializer_class = PizzaSerializer
