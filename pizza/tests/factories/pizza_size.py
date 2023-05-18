import factory

from pizza.models.pizza_size import PizzaSize


class PizzaSizeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PizzaSize
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: f'size_{n}')
