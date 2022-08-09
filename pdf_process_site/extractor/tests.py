from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class FormTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'extractor\home.html')

    def test_form(self):
        response = self.client.post(reverse('home'), {
            'name': "Form_Test",
            'email': 'formtest@gmail.com',
            'upload': 'formtest.pdf',
            'database_url': 'http://formtest',
            'link_url': 'http://formtest'
        })
        self.assertEqual(response.status_code, 200)
