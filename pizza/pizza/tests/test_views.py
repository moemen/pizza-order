from django.urls import reverse

from rest_framework.test import APITestCase

from ..models import Pizza


class PizzaViewsetTest(APITestCase):
    def setUp(self):
        self.pizza = Pizza.objects.create(name='pizza type 1')
        Pizza.objects.create(name='pizza type 2')
        Pizza.objects.create(name='pizza type 3')

    def test_create(self):
        response = self.client.post(reverse('api_v1:pizza-list'))
        self.assertEqual(response.status_code, 405)

    def test_list(self):
        response = self.client.get(reverse('api_v1:pizza-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_retrieve(self):
        response = self.client.get(reverse('api_v1:pizza-detail', kwargs={'pk': self.pizza.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'pizza type 1')

    def test_update(self):
        response = self.client.put(reverse('api_v1:pizza-detail', kwargs={'pk': self.pizza.id}))
        self.assertEqual(response.status_code, 405)

    def test_destroy(self):
        response = self.client.delete(reverse('api_v1:pizza-detail', kwargs={'pk': self.pizza.id}))
        self.assertEqual(response.status_code, 405)
