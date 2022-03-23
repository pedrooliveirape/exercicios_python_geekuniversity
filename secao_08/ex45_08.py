"""
Faça uma função chamada 'desviopadrao' que calcule o desvio padrão de um vetor 'v' contendo 'n' números.
"""
from math import sqrt


def desviopadrao(lista: list):
    listadesvio = []
    listavariancia = []
    # cálculo média:
    media = sum(lista) / len(lista)
    # cálculo desvio:
    for x in range(0, len(lista)):
        if lista[x] > media:
            listadesvio.append(lista[x] - media)
        else:
            listadesvio.append(media - lista[x])
    # cálculo variância:
    for v in range(0, len(listadesvio)):
        listavariancia.append(listadesvio[v] ** 2)
    variancia = sum(listavariancia) / len(lista)
    # cálculo Desvio Padrão:
    desviopadrao = round(sqrt(variancia), 2)
    return desviopadrao
