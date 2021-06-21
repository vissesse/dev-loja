from rest_framework import generics
from app_loja import models
from . import Serializers

# Create your views here.


class TranzacaoViewSet(generics.ListCreateAPIView):
    """
    Endpoint da API que permite que os Tranzações sejam visualizadas ou editadas.
    """
    queryset = models.Tranzacao.objects.all() #query de todas as tranzações
    serializer_class = Serializers.TranzacaoSerializer


class LojaViewSet(generics.ListCreateAPIView):
    """
    Endpoint da API que permite que as lojas sejam visualizadas ou editados.
    """
    queryset = models.Loja.objects.all() #query para mostrar as lojas
    serializer_class = Serializers.LojaSerializer #serializão

    
