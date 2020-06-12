print("="*25)
print("Progressão Aritmética v2.0")
print("="*25)

pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão da PA: "))
a = pt
cont = 1
while cont <= 10:
    print(f"{a} > ", end="")
    a += r
    cont += 1
print("FIM")