"""
Escreva uma função que receba um número inteiro meior do que zero e retorne a soma de todos os seus algoritimos. Por exemplo, ao número 251 corresponderá ao valor 8(2+5+1). Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".

Doctests:

>>> soma_unidades(251)
8
>>> soma_unidades(9)
9
>>> soma_unidades(1000)
1
>>> soma_unidades(0)
Número inválido
"""


def soma_unidades(numero: int):
    if numero < 1:
        print('Número inválido')
    else:
        unidades = str(numero)
        soma = 0
        for c in range(0, len(unidades)):
            soma += int(unidades[c])
        return soma
