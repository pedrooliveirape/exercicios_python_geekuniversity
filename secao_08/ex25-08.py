"""
Faça uma função que receba um inteiro N como parâmetro, calcule e retorne o resultado da seguinte série:
S = 2/4 + 5/5 + 10/6 + ... + (N²+1)/(N+3)

Doctests:

>>> equacao(3)
3.17
>>> equacao(0)
0.0
>>> equacao(37)
616.45
>>> equacao(11)
47.18
>>> equacao(1)
0.5
"""


def equacao(num: int):
    resultado = 0
    for c in range(1, num + 1):
        resultado += (c ** 2 + 1) / (c + 3)
    return float(f'{resultado:.2f}')
