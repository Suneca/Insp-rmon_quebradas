# Função batalha:
def batalha(Vida_Jogador,Vida_Oponente, Poder_Jogador, Defesa_Openente, Poder_Oponente, Defesa_Jogador):
    while Vida_Jogador > 0 and Vida_Oponente > 0:
        while True:
            i2 = input("Você deseja fugir? ")
            probability = randrange(0, 10)
            if probability <= 5:
                print("Taca-le pau nesse carrinho Marcos!!!\n")
                return 2
            else:
                print("vai fugir não vacilão! Aqui é Quebradas truta!!!\n")
        Vida_Oponente = Vida_Oponente - (Poder_Jogador - Defesa_Openente)
        if Vida_Oponente <= 0:
            print("Jogador Ganhou!!!")
            return 1
        Vida_Jogador = Vida_Jogador - (Poder_Oponente - Defesa_Jogador)
        if Vida_Jogador <= 0:
            print("Jogador Perdeu!!!")
            return 0