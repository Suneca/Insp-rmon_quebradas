# -*- coding: utf-8 -*-

insperdex = []

def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"]))
    print("poder = {0}".format(ipmon["poder"]))
    print("vida = {0}".format(ipmon["vida"]))
    print("defesa = {0}\n".format(ipmon["defesa"]))
    
def adiciona_insperdex(numero):
    if not numero in insperdex:
        insperdex.append(numero)


def mostra_insperdex():
    for i in insperdex:
        mostra_ipmon(i)