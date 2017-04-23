# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:04:38 2017

@author: dualstream799
"""
# Importando bibliotecas e funções:
import json
from Inspermon_Quebradas_duelos import luta
# Abrindo arquivo .json:
with open('inspermons.json') as arquivo:
    inspermons = json.load(arquivo)
# Definindo função 'levelup':
def level_up_mon(luta):
    # Parâmetros para a função:
    level = inspescolha["Level"]
    xp = inspescolha["Xp"]
    xp_win = randrange(15, 25)
    xp_lose = randrange(0, 10)
    xp_limit = 100
    # Loop para somar 'XP' ao Inspermon:
    if 1 == luta():
        inspescolha["XP"] += xp_win
    elif 0 == luta():
        inpescolha["XP"] += xp_lose
    # Loop para subir de 'Level' e reiniciar o contador de 'XP':
    if ["XP"] >= xp_limit:
        inspescolha["Level"] += 1
        inspescolha["XP"] - xp_limit
        xp_limit += 25