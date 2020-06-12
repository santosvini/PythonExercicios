print("Primeira e Última String\n")

frase = str(input("Digite a frase: ")).strip().upper()

print("A letra A aparece {} vezes na frase\n".format(frase.count('A')))
print(f"A primeira letra A aparece na posição: {frase.find('A')+1}\n")
print(f"A última letra A aparece na posição: {frase.rfind('A')+1}\n")