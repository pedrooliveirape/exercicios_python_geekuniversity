"""
Faça uma função chamada DesenhaLinha. Ela deve desenhar uma linha na tela usando vários símbolos de igual (Ex:========). A função recebe por parâmetro quantos sinais de igual serão mostrados. Caso não seja desenhado nenhum parâmetro será mostrada uma linha com 20 sinais de =.

doctests:
>>> desenhalinha()
====================
>>> desenhalinha(40)
========================================
>>> desenhalinha(20)
====================
>>> desenhalinha(10)
==========
"""


def desenhalinha(linhas: int = 20):
    lin = str('=' * linhas)
    print(lin)
