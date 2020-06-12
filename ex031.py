print("="*22)
print("Viagem Tarifada - GPS")
print("="*22)

viagem = 200.0
dist = float(input("Qual a distância da sua viagem? "))

if dist <= 200:
    valor = dist * 0.50
    print(f"Sua viagem custará o total de R$ {valor:.2f} reais!")
else:
    dist > 200
    valor = dist * 0.45
    print(f"Sua viagem custara o total de R$ {valor:.2f} reais!")