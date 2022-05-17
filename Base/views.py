from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Instrumento


class HomeView(TemplateView):
    template_name = 'Base/home.html'

# GUITARRA

class GuitarraLista(ListView):
    context_object_name = 'guitarras'
    queryset = Instrumento.objects.filter(instrumento__startswith='guitarra')
    template_name = 'Base/listaGuitarras.html'

class GuitarraDetalle(DetailView):
    model = Instrumento
    context_object_name = 'guitarra'
    template_name = 'Base/guitarraDetalle.html'

class GuitarraUpdate(UpdateView):
    model = Instrumento
    fields = '__all__'
    success_url = reverse_lazy('guitarras')
    context_object_name = 'guitarra'
    template_name = 'Base/guitarraEdicion.html'

class GuitarraDelete(DeleteView):
    model = Instrumento
    success_url = reverse_lazy('guitarras')
    context_object_name = 'guitarra'
    template_name = 'Base/guitarraBorrado.html'

# BAJO

class BajoLista(ListView):
    context_object_name = 'bajos'
    queryset = Instrumento.objects.filter(instrumento__startswith='bajo')
    template_name = 'Base/listaBajos.html'

class BajoDetalle(DetailView):
    model = Instrumento
    context_object_name = 'bajo'
    template_name = 'Base/bajoDetalle.html'

class BajoUpdate(UpdateView):
    model = Instrumento
    fields = '__all__'
    success_url = reverse_lazy('bajos')
    context_object_name = 'bajo'
    template_name = 'Base/bajoEdicion.html'

class BajoDelete(DeleteView):
    model = Instrumento
    success_url = reverse_lazy('bajos')
    context_object_name = 'bajo'
    template_name = 'Base/bajoBorrado.html'

# PEDAL

class PedalLista(ListView):
    context_object_name = 'pedales'
    queryset = Instrumento.objects.filter(instrumento__startswith='pedal')
    template_name = 'Base/listaPedales.html'

class PedalDetalle(DetailView):
    model = Instrumento
    context_object_name = 'pedal'
    template_name = 'Base/pedalDetalle.html'

class PedalUpdate(UpdateView):
    model = Instrumento
    fields = '__all__'
    success_url = reverse_lazy('pedales')
    context_object_name = 'pedal'
    template_name = 'Base/pedalEdicion.html'

class PedalDelete(DeleteView):
    model = Instrumento
    success_url = reverse_lazy('pedales')
    context_object_name = 'pedal'
    template_name = 'Base/pedalBorrado.html'

# AMPLIFICADOR

class AmplificadorLista(ListView):
    context_object_name = 'amplificadores'
    queryset = Instrumento.objects.filter(instrumento__startswith='amplificador')
    template_name = 'Base/listaAmplificadores.html'

class AmplificadorDetalle(DetailView):
    model = Instrumento
    context_object_name = 'amplificador'
    template_name = 'Base/amplificadorDetalle.html'

class AmplificadorUpdate(UpdateView):
    model = Instrumento
    fields = '__all__'
    success_url = reverse_lazy('amplificadores')
    context_object_name = 'amplificador'
    template_name = 'Base/amplificadorEdicion.html'

class AmplificadorDelete(DeleteView):
    model = Instrumento
    success_url = reverse_lazy('amplificadores')
    context_object_name = 'amplificador'
    template_name = 'Base/amplificadorBorrado.html'

# TECLADO

class TecladoLista(ListView):
    context_object_name = 'teclados'
    queryset = Instrumento.objects.filter(instrumento__startswith='teclado')
    template_name = 'Base/listaTeclados.html'

class TecladoDetalle(DetailView):
    model = Instrumento
    context_object_name = 'teclado'
    template_name = 'Base/tecladoDetalle.html'

class TecladoUpdate(UpdateView):
    model = Instrumento
    fields = '__all__'
    success_url = reverse_lazy('teclados')
    context_object_name = 'teclado'
    template_name = 'Base/tecladoEdicion.html'

class TecladoDelete(DeleteView):
    model = Instrumento
    success_url = reverse_lazy('teclados')
    context_object_name = 'teclado'
    template_name = 'Base/tecladoBorrado.html'

# BATERIA

class BateriaLista(ListView):
    context_object_name = 'baterias'
    queryset = Instrumento.objects.filter(instrumento__startswith='bateria')
    template_name = 'Base/listaBaterias.html'

class BateriaDetalle(DetailView):
    model = Instrumento
    context_object_name = 'bateria'
    template_name = 'Base/bateriaDetalle.html'

class BateriaUpdate(UpdateView):
    model = Instrumento
    fields = '__all__'
    success_url = reverse_lazy('baterias')
    context_object_name = 'bateria'
    template_name = 'Base/bateriaEdicion.html'

class BateriaDelete(DeleteView):
    model = Instrumento
    success_url = reverse_lazy('baterias')
    context_object_name = 'bateria'
    template_name = 'Base/bateriaBorrado.html'


# OTRO

class OtroLista(ListView):
    context_object_name = 'otros'
    queryset = Instrumento.objects.filter(instrumento__startswith='otro')
    template_name = 'Base/listaOtros.html'

class OtroDetalle(DetailView):
    model = Instrumento
    context_object_name = 'otro'
    template_name = 'Base/otroDetalle.html'

class OtroUpdate(UpdateView):
    model = Instrumento
    fields = '__all__'
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'Base/otroEdicion.html'

class OtroDelete(DeleteView):
    model = Instrumento
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'Base/otroBorrado.html'


# CREACION INSTRUMENTO

class InstrumentoCreacion(CreateView):
    model = Instrumento
    success_url = reverse_lazy('home')
    fields = '__all__'
    template_name = 'Base/instrumentoCreacion.html'
