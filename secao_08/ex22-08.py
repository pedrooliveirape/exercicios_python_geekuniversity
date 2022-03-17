"""
Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas com postos de exclamação, conforme exemplo abaixo (para n = 5):
!
!!
!!!
!!!!
!!!!!

Doctests:
>>> torreexclamacao(5)
!
!!
!!!
!!!!
!!!!!
>>> torreexclamacao(3)
!
!!
!!!
>>> torreexclamacao(6)
!
!!
!!!
!!!!
!!!!!
!!!!!!
"""


def torreexclamacao(n: int):
    for c in range(1, n+1):
        print(f'{"!"*c}', end="\n")
