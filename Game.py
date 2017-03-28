# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 18:18:18 2017

@author: jhona
"""

import sys

while True:
    
    açao = input('''
    Qual ação deseja realizar?
         dormir ou andar?\n''')
    açao = açao.lower()
    if açao == 'dormir':
        sys.exit(0)
    elif açao == 'andar':
        print ('Você selecionou uma ação inexistente!')
    else:
        erro = input('''
Você selecionou uma ação inexistente!
''')