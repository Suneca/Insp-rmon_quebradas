# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:04:38 2017

@author: dualstream799
"""
# Importando bibliotecas e funções:
import json
from Inspermon_Quebradas_duelos import luta
# Abrindo arquivo .json:
dex = open("inspermons.json", "r+")
print(str(dex))
# Definindo função 'levelup':
def levelup(luta):
    xp = randrange(15, 35)
    if 1 == luta():
        try:
             += xp
        except:
            print("deu ruim")
