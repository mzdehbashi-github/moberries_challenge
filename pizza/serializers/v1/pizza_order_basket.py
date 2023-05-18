from django.db import transaction
from rest_framework import serializers

from pizza.models.pizza_order_basket import PizzaOrderBasket
from pizza.models.order_result import OrderResult
from pizza.models.pizza_order_item import PizzaOrderItem


class OrderResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderResult
        fields = ('date', 'status')
        ref_name = 'PizzaOrderBasketResult'


class PizzaOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PizzaOrderItem
        fields = ('id', 'pizza', 'quantity', 'created_at', 'modified_at')
        read_only_fields = ('id', 'created_at', 'modified_at')
        ref_name = 'PizzaOrderBasketItems'


class PizzaOrderBasketSerializer(serializers.ModelSerializer):
    result = OrderResultSerializer(many=False, read_only=True)
    items = PizzaOrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = PizzaOrderBasket
        fields = ('id', 'customer', 'items', 'result')
        read_only_fields = ('id', 'result')

    def create(self, validated_data):
        with transaction.atomic():
            pizza_order_basket = PizzaOrderBasket.objects.create(
                customer=validated_data['customer'],
            )

            PizzaOrderItem.objects.bulk_create(
                [
                    PizzaOrderItem(
                        pizza=item['pizza'],
                        quantity=item['quantity'],
                        basket=pizza_order_basket,
                    ) for item in validated_data['items']
                ]
            )

        return pizza_order_basket

    def update(self, instance, validated_data):
        raise NotImplementedError
