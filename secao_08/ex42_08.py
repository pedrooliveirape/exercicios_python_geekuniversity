"""
Faça uma função que receba um vetor de reais e retorne a média dele.

Doctests:

>>> mediavetor([1,2,3,4,5])
3.0
>>> mediavetor([9,2,4,6,1,5])
4.5
>>> mediavetor([48,15,16,51,5,65,17,15,6,51])
28.9
"""


def mediavetor(lista: list):
    soma = sum(lista)
    media = soma / len(lista)
    return media
