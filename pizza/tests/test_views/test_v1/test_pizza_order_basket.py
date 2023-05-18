from rest_framework.test import APITestCase

from pizza.tests.factories.pizza import PizzaFactory
from pizza.tests.factories.customer import CustomerFactory
from pizza.models.pizza_order_basket import PizzaOrderBasket


class TestPizzaOrderBasketViewCreate(APITestCase):
    _url = '/pizza/v1/pizza-order-basket/'

    @classmethod
    def setUpTestData(cls):
        cls.pizza_list = PizzaFactory.create_batch(size=2)
        cls.customer = CustomerFactory()

    def test_success(self):
        response = self.client.post(
            self._url,
            data={
                'customer': self.customer.id,
                'items': [
                    {
                        'pizza': pizza.id,
                        'quantity': 2
                    } for pizza in self.pizza_list
                ]
            },
            format='json'
        )

        # Check if response has expected status code
        self.assertEqual(response.status_code, 201)
        pizza_order_basket_id = response.data['id']

        # Check if basket is stored in DB
        pizza_order_basket = PizzaOrderBasket.objects.get(id=pizza_order_basket_id)

        # Check if number of created order items are as expected
        self.assertEqual(pizza_order_basket.pizzaorderitem_set.all().count(), 2)

        # Check if basket does not have related result
        self.assertFalse(hasattr(pizza_order_basket, 'orderresult'))

    def test_fail_pizza_does_not_exist(self):
        response = self.client.post(
            self._url,
            data={
                'customer': self.customer.id,
                'items': [
                    {
                        'pizza': '1000',  # Does not exist
                        'quantity': 2
                    }
                ]
            },
            format='json'
        )

        # Check if response has expected status code
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'items': [{'pizza': ['Invalid pk "1000" - object does not exist.']}]})

    def test_fail_customer_does_not_exist(self):
        response = self.client.post(
            self._url,
            data={
                'customer': '1000',  # Does not exist
                'items': [
                    {
                        'pizza': pizza.id,
                        'quantity': 2
                    } for pizza in self.pizza_list
                ]
            },
            format='json'
        )

        # Check if response has expected status code
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'customer': ['Invalid pk "1000" - object does not exist.']})
