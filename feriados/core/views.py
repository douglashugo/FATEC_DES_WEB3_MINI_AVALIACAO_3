from django.shortcuts import render
from core.models import FeriadoModel
from datetime import date

def feriado(request):
    hoje = date.today()
    feriados = FeriadoModel.objects.filter(mes=hoje.month, dia=hoje.day)
    if feriados:
        feriado = feriados[0]
        data = feriado.get_data()
        return render(request, 'feriado.html', {'feriado': feriado, 'data': data})
    else:
        return render(request, 'nao_e_feriado.html', {'mensagem': 'Hoje não é feriado'})


