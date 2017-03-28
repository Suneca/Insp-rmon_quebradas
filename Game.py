# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:18:18 2017

@author: jhona
"""
import sys
from random import randrange
from Inspermon_Quebradas_duelos import batalha
import json


def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}\n".format(ipmon["defesa"]))

with open('inspermons.json') as arquivo:
    inspermons = json.load(arquivo)

print('''Olá Jogador!!!
Primeiro escolha o seu Inspermon inicial:\n
''')
for ipmon in inspermons:
    mostra_ipmon(ipmon)
escolha = input ('Qual Inspermon mais te chamou a atenção?')

while True:
    
    açao = input('''
    Qual ação deseja realizar?
         dormir ou andar?\n''')
    açao = açao.lower()
    if açao == 'dormir':
        sys.exit(0)
    elif açao == 'andar':
        qual = randrange(0,2)
        batalha()
        
    else:
        erro = input('''
Você selecionou uma ação inexistente!
''')