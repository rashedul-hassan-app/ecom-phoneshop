from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='awklsjf2!')

    def test_opens_success_view(self):
        response = self.client.get(reverse('payment_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success.html')

    def test_opens_cancelled_view(self):
        response = self.client.get(reverse('payment_cancelled'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancelled.html')
