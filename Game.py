# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:18:18 2017

@author: jhonata feat. dualstream799
"""
# Importando bibliotecas e funções:
import sys
from random import randrange
from Inspermon_Quebradas_duelos import batalha
import json
from insperdex import adiciona_insperdex
from insperdex import mostra_insperdex
# Definindo função: Mostras Inspermon:
def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}\n".format(ipmon["defesa"]))
# Fazendo upload do Insperdex:
with open('inspermons.json') as arquivo:
    inspermons = json.load(arquivo)
# Escolhendo Inspermon inicial:
print('''Olá Jogador!!!
Primeiro escolha o seu Inspermon inicial:\n
''')
for ipmon in inspermons:
    mostra_ipmon(ipmon)
while True:
    inspescolha = 0
    escolha = input ('Qual Inspermon mais te chamou a atenção?\n')
    a = 0
    for nome in inspermons:
        if escolha == nome['nome']:
            inspescolha = inspermons[a]
        a += 1
    if inspescolha != 0:
        break
    else:
        print("ERROOUUUU!!! \nDigitou errado meu parça, tente novamente")
# Escolhendo ação do personagem:
while True:
    # Seleção de ação:
    açao = input('''
    Qual ação deseja realizar?
         dormir, andar ou insperdex?\n''')
    açao = açao.lower()
    # Comando 'dormir':
    if açao == 'dormir':
        sys.exit(0)
    # Comando 'andar':
    elif açao == 'andar':
        qual = randrange(0,9)
        mostra_ipmon(inspermons[qual])
        a = input("Você achou um opoente!!! \nAperte Enter para lutar\n\n")
        resultado_batalha = batalha(inspescolha['vida'],inspermons[qual]['vida'],inspescolha['poder'],inspermons[qual]['defesa'],inspermons[qual]['poder'],inspescolha['defesa'])
        if 1 == resultado_batalha:
            adiciona_insperdex(inspermons[qual])
            continue
        elif 2 == resultado_batalha:
            continue
        else:
            break
    # Comando 'visualizar Insperdex':
    elif açao == 'insperdex':
        print (' \n')
        mostra_insperdex()
    # Controle de erro do usuário:
    else:
        erro = input('''
Você selecionou uma ação inexistente!
Aperte Enter para voltar ao menu\n\n''')

