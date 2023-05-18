import factory

from pizza.models.customer import Customer


class CustomerFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Customer

    name = factory.Faker('last_name')
    address = factory.Faker('address')
    phone_number = factory.Sequence(lambda n: f'{n}')
