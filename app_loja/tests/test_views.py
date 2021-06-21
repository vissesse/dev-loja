from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestPagina(TestCase):
    """ Classe de teste"""

    def test_pagina_inicial(self):
        response = self.client.get(reverse('app_loja:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app_loja/index.html")
        self.assertContains(response, "loja")

    def test_lojas(self):
        response = self.client.get(reverse('app_loja:lojas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app_loja/lojas.html",)
        self.assertContains(response, "loja")
     
    def test_loja_tranzacao(self):
        response = self.client.get(reverse('app_loja:loja_trazacoes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app_loja/loja_tranzacao.html",)
        self.assertContains(response, "loja")
     