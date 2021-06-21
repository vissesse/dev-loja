from django.db import models
from . import models


class Tranzacao:

    def tipo_tranzacao(tranzacao):
        t = [
            {'descricao': 'debito', 'natureza': 'entrada', 'sinal': '+'},
            {'descricao': 'boleto', 'natureza': 'saida',  'sinal': '-'},
            {'descricao': 'financiamento', 'natureza': 'saida',  'sinal': '-'},
            {'descricao': 'crédito', 'natureza': 'entrada',  'sinal': '+'},
            {'descricao': 'Recibo emprestimo', 'natureza': 'entrada',  'sinal': '+'},
            {'descricao': 'vendas', 'natureza': 'entrada',  'sinal': '+'},
            {'descricao': 'Recibo TED', 'natureza': 'entrada',  'sinal': '+'},
            {'descricao': 'Recibo DOC', 'natureza': 'entrada',  'sinal': '+'},
            {'descricao': 'Algiel', 'natureza': 'saida',  'sinal': '-'},
        ]

        return t[tranzacao]


class Dados:

    def normalizar(line):
        d = line.decode("utf-8")
        dados = {}
        i = 1
        dado = ''
        for l in str(d):
            if not (l == 'b') and not(l == '\'') and not(l == '\n'):
                if i == 1:
                    dados['tranzacao'] = l
                if 1 < i <= 9:
                    dado += l
                    if len(dado) == 8:
                        dados['data'] = dado
                        dado = ''

                elif 9 < i <= 19:
                    dado += l
                    if len(dado) == 10:
                        dados['valor'] = Tranzacao.tipo_tranzacao(
                            int(dados['tranzacao'])-1)['sinal'] + dado
                        dado = ''

                elif 19 < i <= 30:
                    dado += l
                    if len(dado) == 11:
                        dados['cpf'] = dado
                        dado = ''

                elif 30 < i <= 42:
                    dado += l
                    if len(dado) == 12:
                        dados['cartao'] = dado
                        dado = ''

                elif 42 < i <= 48:
                    dado += l
                    if len(dado) == 6:
                        dados['hora'] = dado
                        dado = ''

                elif 48 < i <= 62:
                    dado += l
                    if len(dado) == 14:
                        dados['dono_loja'] = dado
                        dado = ''
                elif 62 < i <= 81:
                    dado += l
                    if len(dado) == 19:
                        dados['nome_loja'] = dado
                        dado = ''
                i += 1
        return dados


def formatar_hora(hora):
    new_hora = ''
    i = 0
    for h in hora:
        if i == 2 or i == 4:
            new_hora += ':'
        new_hora += h
        i += 1

    return new_hora


def formatar_data(data):
    new_data = ''
    i = 0
    for n in data:
        if i == 4 or i == 6:
            new_data += '-'
        new_data += n
        i += 1
    return new_data


def formatar_cpf(cpf):  
    new_cpf = ''
    i = 0
    for n in cpf:
        if i == 3 or i == 6:
            new_cpf += '.'
        
        if i == 9:
            new_cpf += '-'
            
        new_cpf += n
        i += 1
        
    return new_cpf


def get_dados_do_arquivo(file):
    i = 0
    for line in file:
        dado = Dados.normalizar(line)

        if i != 0:
           # tipo_tranzacao = dado['tranzacao']
            carregar_no_banco(dado)
        i = 1


def carregar_no_banco(dados):
    #

    # tranzicao
    tranzacao_feita = Tranzacao.tipo_tranzacao(int(dados['tranzacao'])-1)

    hora = formatar_hora(dados['hora'])
    data = formatar_data(dados['data'])
    cpf = formatar_cpf(dados['cpf'])
    valor = float(dados['valor'])/100
    cartao = dados['cartao']
    descricao = tranzacao_feita['descricao']
    natureza = tranzacao_feita['natureza']

    # loja
    dono_loja = dados['dono_loja']
    nome_loja = dados['nome_loja']

    try:
        loja = models.Loja.objects.get(
            nome_loja=nome_loja, dono_loja=dono_loja)
    except(KeyError, models.Loja.DoesNotExist):
        loja = models.Loja(nome_loja=nome_loja,
                           dono_loja=dono_loja)
        loja.save()
        loja = models.Loja.objects.get(
            nome_loja=nome_loja, dono_loja=dono_loja)

    try:

        models.Tranzacao.objects.get(loja=loja, descricao=descricao,
                                     natureza=natureza, hora=hora, data=data, valor=valor, cpf=cpf, cartao=cartao)

    except(KeyError, models.Tranzacao.DoesNotExist):
        tranzacao = models.Tranzacao(loja=loja,descricao=descricao,
                                     natureza=natureza,  hora=hora, data=data, valor=valor, cpf=cpf, cartao=cartao)
        tranzacao.save()
