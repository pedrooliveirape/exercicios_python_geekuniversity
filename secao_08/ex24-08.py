"""
Escreva uma função que gera um triângulo de altura e lados n e base 2*n-1. Por exemplo, a saída para n = 6 seria:
     *
    ***
   *****
  *******
 *********
***********

Doctests:

>>> arvorenatal(6)
     *
    ***
   *****
  *******
 *********
***********
>>> arvorenatal(3)
  *
 ***
*****
>>> arvorenatal(8)
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
"""


def arvorenatal(num: int):
    for c in range(0, num):
        espaco = num - (c + 1)
        asterisco = (c * 2) + 1
        print(f"{' ' * espaco}{'*' * asterisco}")
