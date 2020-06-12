print("=-"*9)
print("Programa FATORIAL!")
print("=-"*9)

num = int(input("Digite um valor: "))
cont = num
f = 1
print(f"Calculando {num} fatorial!\n", end="")
while cont > 0:
    print(f"{cont}", end="")
    print(" x " if cont > 1 else " = ", end="")
    f *= cont
    cont -= 1
print(f"Seu fatorial é {f}")