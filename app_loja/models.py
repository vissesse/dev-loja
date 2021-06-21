from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Loja(models.Model):
    nome_loja = models.TextField(max_length=30)
    dono_loja = models.TextField(max_length=30)

    def __str__(self) -> str:
        return 'Nome da loja: %s ---------- Dono da loja:%s ' % (self.nome_loja, self.dono_loja)


class Tranzacao(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    descricao =models.TextField(blank=True)
    natureza = models.TextField(blank=True)
    hora = models.TimeField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    cpf = models.TextField()
    cartao = models.TextField()

    class Meta:
        ordering = ['data', 'hora']

    def __str__(self) -> str:
        return 'Tipo tranzacao: ( %s ) - valor %s' % (self.tipo, self.valor)
