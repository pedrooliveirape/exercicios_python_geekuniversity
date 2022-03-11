"""
Faça uma função que receba a data atual (dia, mês e ano inteiro), e exiba-a na tela no formato textual por extenso.
Exemplo: Data: 01/01/2020, imprimir: 1 de janeiro de 2020.

Doctests

>>> data(1, 1, 2020)
'1 de janeiro de 2020'

>>> data(27, 7, 1988)
'27 de julho de 1988'

>>> data(31, 12, 1993)
'31 de dezembro de 1993'

>>> data(11, 9, 2001)
'11 de setembro de 2001'
"""


def data(dia: int, mes: int, ano: int):
    meses = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
             9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    return f"{dia} de {meses[mes]} de {ano}"

