from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Suggest
import time


def index(request):
    agora = time.localtime()
    foco = time.strptime('16.07.2019', '%d.%m.%Y')
    dias = foco.tm_yday - agora.tm_yday - 1
    horas = 23 - agora.tm_hour
    minutos = 60 - agora.tm_min
    mensagem = 'Faltam ' + str(dias) + ' dias, ' + str(horas) + ' horas e ' + str(minutos) + ' minutos!'
    template = loader.get_template('firstSite/index.html')
    sugestions_list = Suggest.objects.all()
    context = {
        'mensagem': mensagem,
        'sugestions_list': sugestions_list
    }
    return HttpResponse(template.render(context, request))

