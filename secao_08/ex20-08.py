"""
Faça um programa que leia o seu número inteiro n e calcule seu fatorial, n!.

Doctests:

>>> fatotial(5)
120
>>> fatotial(8)
40320
>>> fatotial(10)
3628800
>>> fatotial(2)
2
"""


def fatotial(numero: int):
    fat = 1
    for c in range(1, numero+1):
        fat *= c
    return fat
