from django.urls import reverse

from rest_framework.test import APITestCase

from pizza.pizza.models import Pizza
from ..models import Order


class OrderViewsetTest(APITestCase):
    def setUp(self):
        self.pizza = Pizza.objects.create(
            name='pizza type 1',
            sizes=['30cm', '40cm', '50cm',]
        )
        self.order = Order.objects.create(
            customer_name='Customer Name 1',
            customer_address='diagon alley',
            size='30cm',
            pizza=self.pizza,
        )

    def test_create(self):
        response = self.client.post(
            reverse('api_v1:order-list'),
            data={
                'customer_name': 'Customer Name 2',
                'customer_address': 'diagon alley',
                'size': '50cm',
                'pizza': self.pizza.id,
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 2)

    def test_create_with_invalid_size(self):
        response = self.client.post(
            reverse('api_v1:order-list'),
            data={
                'customer_name': 'Customer Name 2',
                'customer_address': 'diagon alley',
                'size': '70cm',  # No pizza with this size
                'pizza': self.pizza.id,
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Order.objects.count(), 1)

    def test_list(self):
        response = self.client.get(
            reverse('api_v1:order-list'),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_retrieve(self):
        response = self.client.get(
            reverse('api_v1:order-detail', kwargs={'pk': self.order.id}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['customer_name'], 'Customer Name 1')

    def test_update(self):
        response = self.client.put(
            reverse('api_v1:order-detail', kwargs={'pk': self.order.id}),
            data={
                'customer_name': 'Customer Name 3',
                'customer_address': 'diagon alley',
                'size': '50cm',
                'pizza': self.pizza.id,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['customer_name'], 'Customer Name 3')

    def test_partial_update(self):
        response = self.client.patch(
            reverse('api_v1:order-detail', kwargs={'pk': self.order.id}),
            data={
                'customer_name': 'Customer Name 3',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['customer_name'], 'Customer Name 3')
        self.assertEqual(response.json()['customer_address'], 'diagon alley')

    def test_destroy(self):
        response = self.client.delete(
            reverse('api_v1:order-detail', kwargs={'pk': self.order.id}),
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Order.objects.count(), 0)
