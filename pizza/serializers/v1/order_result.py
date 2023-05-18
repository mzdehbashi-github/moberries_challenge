from rest_framework import serializers


from pizza.models.order_result import OrderResult


class OrderResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderResult
        fields = ('id', 'status')

    def create(self, validated_data):
        raise NotImplementedError
