print("=========================")
print("Jogo da Adivinhação v2.0")
print("=========================")

from random import randint

comp = randint(0, 10)
print("Tente acertar o número que eu processei de 0 a 10....\n")
acertou = False
palpite = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite: "))
    palpite += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print("Mais....")
        else:
            jogador > comp
            print("Menos....Tente de novo!")
print(f"Acertou com {palpite} tentativas, Parabéns!")

