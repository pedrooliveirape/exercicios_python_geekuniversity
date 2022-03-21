"""
Faça uma função 'Troque' que recebe dua variáveis reais A e B e troca o valor delas (i.e., A recebe o valor de B e B recebe o valor de A).

Doctests:

>>> troca(2, 3)
(3, 2)
>>> troca(125, 454)
(454, 125)
>>> troca(92, 48)
(48, 92)
"""


def troca(a: int, b: int):
    x = a
    a = b
    b = x
    return a, b
