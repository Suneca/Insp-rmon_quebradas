# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:18:18 2017

@author: jhona
"""
import sys
from random import randrange
from Inspermon_Quebradas_duelos import batalha
import json
from insperdex import adiciona_insperdex
from insperdex import mostra_insperdex

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
escolha = input ('Qual Inspermon mais te chamou a atenção?\n')

a = 0
for nome in inspermons:
    if escolha == nome['nome']:
        inspescolha = inspermons[a]
    a += 1

while True:
    
    açao = input('''
    Qual ação deseja realizar?
         dormir, andar ou insperdex?\n''')
    açao = açao.lower()
    
    if açao == 'dormir':
        sys.exit(0)
        
    elif açao == 'andar':
        qual = randrange(0,9)
        mostra_ipmon(inspermons[qual])
        a = input("Você achou um opoente!!! \nAperte Enter para lutar\n\n")
        if 1 == batalha(inspescolha['vida'],inspermons[qual]['vida'],inspescolha['poder'],inspermons[qual]['defesa'],inspermons[qual]['poder'],inspescolha['defesa']):
            adiciona_insperdex(inspermons[qual])
            continue
        else:
            break
    elif açao == 'insperdex':
        print (' \n')
        mostra_insperdex()
        
    else:
        erro = input('''
Você selecionou uma ação inexistente!
Aperte Enter para voltar ao menu\n\n''')
        