"""
Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o hiperfatorial desse número.

Doctests:

>>> hiperfatorial(4)
27648
>>> hiperfatorial(2)
4
>>> hiperfatorial(1)
1
>>> hiperfatorial(3)
108
"""


def hiperfatorial(num: int):
    hiper = 1
    for c in range(1, num+1):
        hiper *= c ** c
    return hiper
