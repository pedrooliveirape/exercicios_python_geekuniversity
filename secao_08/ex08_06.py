"""
Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segundos, e os converta em segundos.

Doctests:

>>> segundos(1, 30,52)
5452
>>> segundos(3,48,14)
13694
>>> segundos(2,25,30)
8730
"""


def segundos(hora: int, minuto: int, segundo: int):
    min = minuto + (hora*60)
    seg = segundo + (min*60)
    return seg

