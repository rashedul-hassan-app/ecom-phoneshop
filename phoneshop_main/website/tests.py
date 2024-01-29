from django.test import TestCase
from .models import Category, Customer, Product, Order

# Category Model tests


class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Android')

    def test_string_representation(self):
        category = Category.objects.get(name='Android')
        self.assertEqual(str(category), 'Android')


class CustomerModelTest(TestCase):
    def setUp(self):
        Customer.objects.create(
            first_name='Jennifer',
            last_name='Ann',
            phone='00737377337',
            email='jennifer@django.com',
            password='somepass'
        )

    def test_string_representation(self):
        customer = Customer.objects.get(email='jennifer@django.com')
        self.assertEqual(str(customer), 'Jennifer Ann')


class ProductModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Electronics')
        Product.objects.create(
            name='MacBook',
            price=1999,
            category=category,
            description='Apple macbook',
            is_sale=True,
            sale_price=1799
        )
        Product.objects.create(
            name='iPad',
            price=999,
            category=category,
            description='Apple iPad',
            is_sale=False,
        )

    def test_string_representation(self):
        product = Product.objects.get(name='MacBook')
        self.assertEqual(str(product), 'MacBook')

    def test_sale_price_true(self):
        product = Product.objects.get(name='MacBook')
        self.assertTrue(product.is_sale)

    def test_sale_price_false(self):
        product = Product.objects.get(name='iPad')
        self.assertFalse(product.is_sale)
