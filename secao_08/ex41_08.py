"""
Faça uma função que receba um vetor de inteiros e retorne o maior valor.

Doctests:

>>> maiorvalor([1,4,3,9,6,5,7,8,2])
9
>>> maiorvalor([5,4,3,2,1])
5
>>> maiorvalor([10,20,30,40,50,60])
60
"""


def maiorvalor(lista: list):
    maior = 0
    for n in range(0, len(lista)):
        if maior < lista[n]:
            maior = lista[n]
    return maior
