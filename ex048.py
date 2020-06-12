print("#################")
print("Nº Múltiplos de 3")
print("#################")

#num = int(input("\nDigite um número multiplo de 3: "))
#print(f"O número {num} é um número múltiplo de 3")
s = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        cont += 1
        s = s + num
print(f"A soma dos {cont}, dá o somatório de {s}")
print("FIM")
