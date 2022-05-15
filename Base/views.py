from django.views.generic import TemplateView, ListView
from .models import Instrumento

class HomeView(TemplateView):
    template_name = 'Base/home.html'

class GuitarraLista(ListView):
    context_object_name = 'guitarras'
    queryset = Instrumento.objects.filter(tipoInstrumento__startswith='gui')
    template_name = 'Base/listaGuitarras.html'

class BajoLista(ListView):
    context_object_name = 'bajos'
    queryset = Instrumento.objects.filter(tipoInstrumento__startswith='baj')
    template_name = 'Base/listaBajos.html'

class PedalLista(ListView):
    context_object_name = 'pedales'
    queryset = Instrumento.objects.filter(tipoInstrumento__startswith='ped')
    template_name = 'Base/listaPedales.html'

class BateriaLista(ListView):
    context_object_name = 'baterias'
    queryset = Instrumento.objects.filter(tipoInstrumento__startswith='bat')
    template_name = 'Base/listaBaterias.html'

class TecladoLista(ListView):
    context_object_name = 'teclados'
    queryset = Instrumento.objects.filter(tipoInstrumento__startswith='tec')
    template_name = 'Base/listaTeclados.html'

class AmplificadorLista(ListView):
    context_object_name = 'amplificadores'
    queryset = Instrumento.objects.filter(tipoInstrumento__startswith='amp')
    template_name = 'Base/listaAmplificadores.html'




