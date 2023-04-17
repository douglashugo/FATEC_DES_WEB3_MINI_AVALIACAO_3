from django.db import models
from datetime import date

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado', max_length=80)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mes')

    def get_data(self):
        # assume que o ano do feriado é o ano corrente
        ano_atual = date.today().year
        return date(ano_atual, self.mes, self.dia)

    def __str__(self):
        return self.nome
