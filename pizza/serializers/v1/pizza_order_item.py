from rest_framework import serializers

from pizza.models.pizza_order_item import PizzaOrderItem


class PizzaOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PizzaOrderItem
        fields = ('pizza', 'quantity')

    def create(self, validated_data):
        raise NotImplementedError
