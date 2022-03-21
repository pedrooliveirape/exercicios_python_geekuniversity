"""
Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número. Um fatorial exponencial é um inteiro positivo n elevado a potência de n-1, que por sua vez é elevado a potência de n-2 e assim em diante.

Doctests:

>>> fatexponencial(1)
1
>>> fatexponencial(3)
9
>>> fatexponencial(4)
262144
>>> fatexponencial(2)
2
"""


def fatexponencial(num: int):
    fat = 1
    for n in range(2, num+1):
        fat = n ** (fat)
    return fat
