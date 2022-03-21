"""
Faça uma função que recebe um vetor de inteiros e retorne quantos valores pares ele possui.

Doctests:

>>> vetor([1,2,3,4,5])
2
>>> vetor([5,6,8,14,6,123,456])
5
>>> vetor([65,5,73,645,85])
0
"""


def vetor(lista: list):
    pares = 0
    for c, v in enumerate(lista):
        if v % 2 == 0:
            pares += 1
    return pares
