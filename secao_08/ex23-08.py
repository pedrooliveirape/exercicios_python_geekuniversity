"""
Escreva uma função que dera um triângulo lateral de altura 2*n-1 e n largura. Por exemplo, a saída para n=4 seria:
*
**
***
****
***
**
*

Doctests:

>>> triangulolateral(4)
*
**
***
****
***
**
*
>>> triangulolateral(0)

>>> triangulolateral(3)
*
**
***
**
*
>>> triangulolateral(1)
*
"""


def triangulolateral(n: int):
    for c in range(1, n+1):
        print(f"{'*'*c}", end="\n")
    for l in range(n-1, 0, -1):
        print(f"{('*'*l)}")
