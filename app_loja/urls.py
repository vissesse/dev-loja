
from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'app_loja'
urlpatterns = [
    path('', views.carregar_arquivo, name='index'),
    path('lojas/', views.loja, name='lojas'),
    path('lojas/<int:pk>/tranzacao/', views.loja_tranzacao, name='loja_trazacoes'),
]
