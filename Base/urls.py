from django.urls import path
from Base.views import AmplificadorLista, TecladoLista, BateriaLista, BajoLista, GuitarraLista, HomeView, PedalLista

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('listaGuitarras/', GuitarraLista.as_view(), name='guitarras'),
    path('listaBajos/', BajoLista.as_view(), name='bajos'),
    path('listaPedales/', PedalLista.as_view(), name='pedales'),
    path('listaBaterias/', BateriaLista.as_view(), name='baterias'),
    path('listaTeclados/', TecladoLista.as_view(), name='teclados'),
    path('listaAmplificadores/', AmplificadorLista.as_view(), name='amplificadores'),
]
