print("Lendo Nome Completo\n")


#Lendo o nome completo
n = str(input("Digite seu nome completo: ")).strip().upper()
nome = n.split()
print(nome)
# Ler o primeiro nome
print(f"Primeiro Nome: {(nome[0])}")
# Ler o nome do meio
print(f"Nome do meio: {nome[1]}")
# Ler o terceiro nome
print(f"Último Nome: {nome[2]}")