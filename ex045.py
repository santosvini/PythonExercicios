print("="*10)
print("JÓ-KEN-PÔ")
print("="*10)

from random import randint
from time import sleep
elementos = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print("Escolha seu elemento no jogo: \n"
      "[0] PEDRA\n"
      "[1] PAPEL\n"
      "[2] TESOURA\n")
escolha = int(input(f"Escolha a sua jogada: "))

print("=-"*15)
print(f"O computador escolheu: {elementos[computador]}")
print(f"O jogador escolheu: {elementos[escolha]}")
print("-="*15)

print("JÓ")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
print("+"*14)

# Computador jogou PEDRA
if computador == 0:
    if escolha == 0:
        print("EMPATE!")
    elif escolha == 1:
        print("Jogador GANHOU")
    elif escolha == 2:
        print("Computador GANHOU")
    else:
        print("Opção inválida")
# Computador jogou PAPEL
elif computador == 1:
    if escolha == 0:
        print("Computador GANHOU")
    elif escolha == 1:
        print("EMPATE")
    elif escolha == 2:
        print("Jogador GANHOU")
    else:
        print("Opção Inválida")
# Computador jogou TESOURA
elif computador == 2:
    if escolha == 0:
        print("Jogador GANHOU")
    elif escolha == 1:
        print("Computador GANHOU")
    elif escolha == 2:
        print("EMPATE")
    else:
        print("Opção Inválida!")
