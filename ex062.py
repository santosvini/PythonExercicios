print("="*25)
print("Super Progressão Aritmética v3.0")
print("="*25)

pt = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão da PA: "))
a = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{a} > ", end="")
        a += r
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos mostrados!")
print("FIM")