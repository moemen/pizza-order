from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Pizza


class PizzaTest(TestCase):
    def test_create(self):
        pizza = Pizza.objects.create(
            name='Test Pizza',
            sizes=['30cm', '40cm', '50cm',]
        )
        pizza.full_clean()  # This should just success

    def test_create_with_invalid_size(self):
        pizza = Pizza(
            name='Test Pizza',
            sizes=['30cm', '40cm', '50cm', '70cm']
        )
        with self.assertRaises(ValidationError):  # No pizza with 70cm
            pizza.full_clean()
