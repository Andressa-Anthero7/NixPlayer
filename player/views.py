from django.shortcuts import render, get_object_or_404
from .models import Biblicoteca
from django.http import HttpResponse


# Create your views here.

def index(request):
    faixas_album = Biblicoteca.objects.order_by('?')
    return render(request, 'player/index.html', {'faixas_album': faixas_album})


def adicionar_audio(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        Biblicoteca.objects.create(nome_musica=my_file, midia=my_file)
        return HttpResponse('Tudo Salvo Feliz Natal Andressa..Vai tomar uma cervejinha kkkkkkk')

        # Biblicoteca.objects.create(midia=my_file)
        return HttpResponse('Audio Adicionado')
    else:
        return render(request, 'player/adicionar_audio.html')
