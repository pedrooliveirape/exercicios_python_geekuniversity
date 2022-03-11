"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa a² + b² = c², Faça uma função que receba os valores de a e b e calcule ovalor da hipotenusa através da equação.

doctestes:

>>> hipotenusa(12,16)
20.0
>>> hipotenusa(16,20)
25.6
>>> hipotenusa(8,10)
12.8
"""
from math import sqrt


def hipotenusa(a: int, b: int):
    raizhip = (a ** 2)+(b ** 2)
    hip = sqrt(raizhip)
    hip = float(f'{hip:.1f}')
    return hip
