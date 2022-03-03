"""
Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado perfeito é um número inteiro não
negativo que pode ser expresso como o quadrado de outro número inteiro. Ex: 1, 4, 9...

Doctests:

>>> quadrado(9)
True
>>> quadrado(78)
False
>>> quadrado(81)
True
>>> quadrado(36)
True
"""
from math import sqrt


def quadrado(num: int):
    if sqrt(num) % 1 == 0:
        resp = True
    else:
        resp = False
    return resp
