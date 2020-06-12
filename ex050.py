print("@"*32)
print("Somando números pares inteiros!")
print("@"*32)

s = 0
cont = 0
for x in range(1, 7):
    num = int(input(f"Digite o {x}º valor: "))
    if (num % 2) == 0:
        s += num
        cont += 1
print(f"{cont} números são pares e a soma deles é: {s}")
