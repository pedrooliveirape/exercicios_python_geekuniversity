"""
Faça uma função chamada 'simplifica' que recebe o numerador e o denominador de uma fração. Esta função deve simploficar a fração recebida deividindo o numerador e o denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e o denominador por 12. A função deve modificar as variáveis passadas como parâmetro.

Doctests:

>>> simplifica(36,60)
(3, 5)
>>> simplifica(24,12)
(2, 1)
>>> simplifica(69,92)
(3, 4)
"""


def simplifica(numerador: int, denominador: int):
    div = numerador

    while True:
        if numerador % div == 0 and denominador % div == 0:
            numerador = int(numerador / div)
            denominador = int(denominador / div)
            return numerador, denominador
        else:
            div -= 1
