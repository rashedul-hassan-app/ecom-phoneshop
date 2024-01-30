from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Customer, Product, Order
from django.contrib.auth.models import User

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


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='awklsjf2!')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_add_product_view_not_available_for_non_admin(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)

    def test_404(self):
        response = self.client.get('/random-url-that-doesnt-exist')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')


class AdminViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            username='asdf', password='123456789!', email='test@gmail.com')
        self.client.login(username='asdf', password='123456789!')

    def test_add_product_view_opens_for_admin(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_product.html')
