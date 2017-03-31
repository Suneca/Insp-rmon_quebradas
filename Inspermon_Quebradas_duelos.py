# Importando random range:
from random import randrange
# Definindo ação: CORRER ou LUTAR?
def fugir():
    i2 = input("Você deseja fugir? ")
    while True:
        if i2 == "Sim":
            print("Vazilhão\n\n  ")
            probability = randrange(0, 10)
            while True:
                if probability <= 5:
                    print("Taca-le pau nesse carrinho Marcos!!!\n")
                    return 2
                else:
                    print("vai fugir não vacilão! Aqui é Quebradas truta!!!\n")
                    return 3
        elif i2 == "Não":
            i3 = input("Boa monstro!!! \nHora do show pohaaa!!!!\n")
            return 3
        else:
            print("Responda Sim ou Não, parça\n")
            return
# Função luta:
def luta(Vida_Jogador,Vida_Oponente, Poder_Jogador, Defesa_Openente, Poder_Oponente, Defesa_Jogador):
    while Vida_Jogador > 0 and Vida_Oponente > 0:
        Vida_Oponente = Vida_Oponente - (Poder_Jogador - Defesa_Openente)
        if Vida_Oponente <= 0:
            print("Jogador Ganhou!!!")
            return 1
        Vida_Jogador = Vida_Jogador - (Poder_Oponente - Defesa_Jogador)
        if Vida_Jogador <= 0:
            print("Jogador Perdeu!!!")
            return 0
# Dando "merge":
def batalha(Vida_Jogador,Vida_Oponente, Poder_Jogador, Defesa_Openente, Poder_Oponente, Defesa_Jogador):
    if 3 == fugir():
        return luta(Vida_Jogador,Vida_Oponente, Poder_Jogador, Defesa_Openente, Poder_Oponente, Defesa_Jogador)
