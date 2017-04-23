# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:29:49 2017

@author: dualstream799
"""

# Importando  bibliotecas:
import json
# Importando Funções:
from Inspermon_Quebradas_duelos import luta
# Definindo função: Level System:
def level_up_player(luta):
    # Parâmetros para a função:
    Character_Status = {"Level":0, "XP":0}
    xp_win = randrange(25, 35)
    xp_lose = randrange(5, 15)
    xp_limit = 300
    # Loop para somar 'XP' ao Personagem:
    if 1 == luta():
        Character_Status["XP"] += xp_win
    elif 0 == luta():
        Character_Status["XP"] += xp_lose
    # Loop para subir de 'Level' e reiniciar o contador de 'XP':
    if Character_Status["XP"] >= xp_limit:
        Character_Status["Level"] +=1
        Character_Status["XP"] - xp_limit
        xp_limit += 50