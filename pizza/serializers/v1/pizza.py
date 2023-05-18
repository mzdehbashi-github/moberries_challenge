from rest_framework import serializers

from pizza.models.pizza import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    flavour = serializers.SlugRelatedField(slug_field='name', read_only=True)
    size = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Pizza
        fields = ('id', 'flavour', 'size')
