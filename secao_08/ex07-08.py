"""
Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida em graus Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

Doctests:

>>> conversorTemperatura(5)
41.0
>>> conversorTemperatura(32)
89.6
>>> conversorTemperatura(0)
32.0
"""


def conversorTemperatura(celsius: int):
    fahrenheit = celsius*(9/5)+32
    return fahrenheit