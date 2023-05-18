from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.exceptions import ValidationError

from pizza.models.pizza_order_item import PizzaOrderItem
from pizza.serializers.v1.pizza_order_item import PizzaOrderItemSerializer


class PizzaOrderItemView(GenericViewSet, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = PizzaOrderItem.objects.all().select_related('basket__orderresult', 'basket')
    serializer_class = PizzaOrderItemSerializer

    def get_object(self):
        order_item: PizzaOrderItem = super().get_object()
        if self.action in ('destroy', 'update', 'partial_update'):
            if order_item.basket.result:
                raise ValidationError(
                    {'detail': 'Can not change/delete this record, since the related basket has result'}
                )

        return order_item
