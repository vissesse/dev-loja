from django.test import TestCase
from django.urls.base import reverse

# Create your tests here.

class TestApi(TestCase):
    """ Classe de teste"""

    def test_loja_api(self):
        response = self.client.get(reverse('app_loja_api:api_lojas'))
        self.assertEqual(response.status_code, 200)
        
    def test_tranzacoes_api(self):
        response = self.client.get(reverse('app_loja_api:api_tranzacao'))
        self.assertEqual(response.status_code, 200)
        
   
     