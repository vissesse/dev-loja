from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from . import Forms, models
from . import normalizar


# Create your views here.

def carregar_arquivo(request):

    if request.method == "POST":
        form = Forms.FormFile(request.POST, request.FILES)
        if form.is_valid():
            normalizar.get_dados_do_arquivo(request.FILES["arquivo"])

            return HttpResponseRedirect(reverse('app_loja:lojas'))
    else:
        form = Forms.FormFile()
    return render(request, "app_loja/index.html", {"form": form})


def loja(request):
    lojas = models.Loja.objects.all()

    return render(request, "app_loja/lojas.html", {'lojas': lojas})


def loja_tranzacao(request, pk):

    tranzacoes_queryset = models.Tranzacao.objects.filter(
        loja=pk).order_by('-data', '-hora')
    if not tranzacoes_queryset:
        return HttpResponseRedirect((reverse('app_loja:index')))

    saldo_total = 0
    tranzacoes = []
    for tranzacao in tranzacoes_queryset:
        nome_loja = tranzacao.loja.nome_loja
        dono_loja = tranzacao.loja.dono_loja
        saldo_total += tranzacao.valor

        t_dic = {'descricao': tranzacao.descricao,
                 'natureza': tranzacao.natureza,
                 'hora': tranzacao.hora,
                 'data': tranzacao.data,
                 'valor': tranzacao.valor,
                 'cpf': tranzacao.cpf,
                 'cartao': tranzacao.cartao

                 }

        tranzacoes.append(t_dic)

    loja = {
        'nome_loja': nome_loja,
        'dono_loja': dono_loja
    }

    return render(request, 'app_loja/loja_tranzacao.html', {'tranzacoes': tranzacoes, 'saldo_total': saldo_total, 'loja': loja})
