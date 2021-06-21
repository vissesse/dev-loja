from django.db.models import fields
from rest_framework import serializers

from app_loja import models


class TranzacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tranzacao
        fields = ['id', 'loja', 'tipo', 'hora',
                  'data', 'cpf', 'cartao', 'valor']


class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Loja
        fields = ['id','nome_loja', 'dono_loja']
