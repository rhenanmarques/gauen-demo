from django.test import TestCase
from django.urls import reverse

class GauenPublicURLsTest(TestCase):
    def test_the_pytest_is_ok(self):
        ...

    def test_public_home_url_is_correct(self):
        url = reverse('gauenPublic:home')
        self.assertEqual(url, '/')

    def test_public_contacto_url_is_correct(self):
        url = reverse('gauenPublic:contact')
        self.assertEqual(url, '/contacto/')