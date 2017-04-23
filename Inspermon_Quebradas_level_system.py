# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:29:49 2017

@author: dualstream799
"""

# Importando  bibliotecas:
import json
# Importando Funções:
from Inspermon_Quebradas_duelos import luta
# Abrindo arquivo .json:
with open('Character.json') as arquivo:
    status = json.load(arquivo)
# Definindo função para aumentar o XP do personagem:
def level_up_player(luta):
    # Parâmetros para a função:
    level = status["Level"]
    exp = status["XP"]
    xp_win = randrange(25, 35)
    xp_lose = randrange(5, 15)
    xp_limit = 300
    # Loop para somar 'XP' ao Personagem:
    if 1 == luta():
        exp += xp_win
    elif 0 == luta():
        exp += xp_lose
    # Loop para subir de 'Level' e reiniciar o contador de 'XP':
    if Character_Status["XP"] >= xp_limit:
        level += 1
        exp = exp - xp_limit
        xp_limit += 50