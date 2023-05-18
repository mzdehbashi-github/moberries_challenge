import factory

from pizza.models.pizza_flavour import PizzaFlavour


class PizzaFlavourFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = PizzaFlavour
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: f'name{n}')
