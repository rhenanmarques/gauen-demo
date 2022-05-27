from django.test import TestCase
from django.urls import reverse, resolve
from gauenPublic import views

class GauenPublicViewsTest(TestCase):
    def test_gauenPublic_home_view_function_is_correct(self):
        view = resolve(reverse('gauenPublic:home'))
        self.assertIs(view.func, views.home)

    def test_gauenPublic_contacto_view_function_is_correct(self):
        view = resolve(reverse('gauenPublic:contact'))
        self.assertIs(view.func, views.contact)

    def test_gauenPublic_home_view_returns_status_code_200_ok(self):
        '''Realiza o teste de status code da operação'''
        response = self.client.get(reverse('gauenPublic:home'))
        self.assertEqual(response.status_code, 200)

    def test_gauenPublic_home_view_loads_correct_template(self):
        '''Realiza a verificação se o template renderizado foi o correto'''
        response = self.client.get(reverse('gauenPublic:home'))
        self.assertTemplateUsed(response, 'gauenPublic/pages/home.html')


