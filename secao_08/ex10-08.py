"""
Faça uma função que receba dois números e retorne qual deles é o maior.

Doctests:

>>> maior_menor(5,3)
5
>>> maior_menor(7,9)
9
>>> maior_menor(95756,5516)
95756
>>> maior_menor(875,875)
875
"""


def maior_menor(a: int, b: int):
    if a > b:
        return a
    else:
        return b
