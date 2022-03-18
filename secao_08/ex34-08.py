"""
Faça uma função não-recursiva que receba um número inteiro positivo ímpar N e retorne o fatorial duplo desse número. O fatorial duplo é definido como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5! = 1 * 3 * 5 = 15.

Doctests:

>>> fatduplo(5)
15
>>> fatduplo(9)
945
>>> fatduplo(1)
1
>>> fatduplo(27)
213458046676875
"""


def fatduplo(n: int):
    fat = 1
    for c in range(1, n+1, 2):
        fat *= c
    return fat
