print("======================")
print("RADAR ELETRÔNICO!")
print("======================")

limite = 80.0
multa = 7

velocidade = float(input("Qual a sua velocidade: "))

if velocidade <= limite:
    print("Boa Tarde, cuidado na estrada, siga viagem!")
else:
    valor = (velocidade - limite) * 7
    print(f"Você ultrapassou o limite de velocidade e foi multado em {valor:.2f} reais!")