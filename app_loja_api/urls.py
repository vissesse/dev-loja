from django.urls import path
from . import views

app_name="app_loja_api"
urlpatterns = [
    path('loja/', views.LojaViewSet.as_view(), name='api_lojas'), #rota para r lojas
    path('loja/tranzacoes/', views.TranzacaoViewSet.as_view(), name='api_tranzacao'), #rota das tranzacões
]
