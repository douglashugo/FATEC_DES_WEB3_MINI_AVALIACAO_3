from datetime import date
from django.test import TestCase, Client
from django.urls import reverse
from .models import FeriadoModel


def setUp(self):
    self.client = Client()

def test_feriado(self):
    hoje = date.today()
    feriado = FeriadoModel.objects.create(nome='Teste', mes=hoje.month, dia=hoje.day)
    url = reverse('feriado')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'feriado.html')
    self.assertEqual(response.context['feriado'], feriado)
    self.assertEqual(response.context['data'], feriado.get_data())

def test_nao_e_feriado(self):
    hoje = date.today()
    url = reverse('feriado')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'nao_e_feriado.html')
    self.assertEqual(response.context['mensagem'], 'Hoje não é feriado')
