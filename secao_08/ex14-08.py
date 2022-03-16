"""
Faça uma função que receba a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule em Km/l e escreva uma mensagem de acordo com a tabela a baixo:
CONSUMO   | (Km/l) | MENSAGEM
menor que |    8   | Venda o carro!
entre     | 8 e 12 | Econômico!
maior que |   12   | Super econômico!

Doctests:

>>> kmlitro(300,40)
Venda o carro!
>>> kmlitro(150,13)
Econômico!
>>> kmlitro(800, 84)
Econômico!
>>> kmlitro(500,26)
Super econômico!
"""


def kmlitro(km: int, litro: int):
    consumo = km/litro
    if consumo > 12:
        print('Super econômico!')
    elif 12 > consumo >= 8:
        print('Econômico!')
    else:
        print('Venda o carro!')
