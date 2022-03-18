"""
Faça uma função não recursiva que receba um número inteiro positivo n e retorne o fatorial quádruplo desse número. O fatorial quádruplo de um número n é dado por: (2n)!/n!.

Doctests:

>>> fatquadruplo(2)
12
>>> fatquadruplo(6)
665280
>>> fatquadruplo(1)
2
>>> fatquadruplo(3)
120
"""


def fatquadruplo(n: int):
    n2 = n * 2
    fatnum = 1
    fatden = 1
    for c in range(1, n+1):
        fatden *= c
    for i in range(1, n2+1):
        fatnum *= i
    fat = int(fatnum/fatden)
    return fat
