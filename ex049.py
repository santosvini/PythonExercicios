print("x"*25)
print("Bem-Vindo a Tabuada v2.0")
print("x"*25)

n = int(input("Digite um número para a tabuada: "))
for t in range(1, 11):
    print(f"{n} x {t:2} = {n*t}")