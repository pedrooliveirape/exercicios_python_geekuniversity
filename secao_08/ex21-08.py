"""
Faça uma função para determinar a quantidade de números primos abaixo de N.

Doctests:

>>> primos(6)
3
>>> primos(16)
6
>>> primos(40)
12
>>> primos(87)
23
>>> primos(2)
0
"""


def primos(n: int):
    qtdprimos = 0
    for numeros in range(1, n):
        div = 0
        for p in range(1, numeros+1):
            if numeros % p == 0:
                div += 1
        if div == 2:
            qtdprimos += 1
    return qtdprimos
