"""
Faça um programa contendo as seguintes funções que recebam um vetor V números reais como parâmetro:
- Impressão normal do vetor (função chamada 'normal()').
- Impressão inversa (função chamada 'inversa()').
- Função chamada 'media()' que retorna a média aritimética dos elementos do vetor.
"""


def normal(lista: list):
    print(lista)


def inversa(lista: list):
    inverte = lista.sort(reverse=True)
    print(inverte)


def media(lista: list):
    mediaa = sum(lista) / len(lista)
    return mediaa
