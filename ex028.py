print("=========================")
print("Jogo da Adivinhação v1.0")
print("=========================")

from random import randint
from time import sleep

comp = randint(0, 5)
print("Tente adivinhar o número que eu pensei....\n")
jogador = int(input("Qual número eu pensei: "))
sleep(0.5)

if jogador == comp:
    print(f"Parabéns, você acertou....eu pensei no Nº: {jogador}")
else:
    print(f"Você errooooooou.....eu pensei no Nº: {comp} e não no Nº: {jogador}")