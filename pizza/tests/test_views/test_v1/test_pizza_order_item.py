from rest_framework.test import APITestCase

from pizza.tests.factories.order_result import OrderResultFactory
from pizza.tests.factories.pizza_order_item import PizzaOrderItemFactory
from pizza.tests.factories.pizza import PizzaFactory


class TestPizzaOrderItemView(APITestCase):
    _url = '/pizza/v1/pizza-order-item/'

    @classmethod
    def setUpTestData(cls):
        cls.pizza_order_item = PizzaOrderItemFactory(
            quantity=2
        )

    def test_update_item_success(self):
        new_pizza = PizzaFactory()
        update_data = {
            'pizza': new_pizza.id,
            'quantity': 10
        }

        response = self.client.patch(
            f'{self._url}{self.pizza_order_item.id}/',
            data=update_data,
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        self.pizza_order_item.refresh_from_db()
        self.assertEqual(self.pizza_order_item.pizza, new_pizza)
        self.assertEqual(self.pizza_order_item.quantity, 10)

    def test_update_fail_because_basket_has_result(self):
        OrderResultFactory(basket=self.pizza_order_item.basket)
        response = self.client.patch(
            f'{self._url}{self.pizza_order_item.id}/',
            data={'quantity': 1},
            format='json',
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {'detail': 'Can not change/delete this record, since the related basket has result'}
        )

    def test_update_fail_because_record_does_not_exist(self):
        OrderResultFactory(basket=self.pizza_order_item.basket)
        response = self.client.patch(
            f'{self._url}1000/',
            data={'quantity': 1},
            format='json',
        )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'Not found.'})
