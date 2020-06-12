print("Aluguel de Carros!")

# 1 Qunatidade de dias de aluguel

dias = int(input("Quantos dias de aluguel: "))

# 2 Quantidade de KM rodados

km = float(input("Digite a KM percorrida: "))

# 3 Valores

kmrodado = 0.15
aluguel = 60

preco = (km * kmrodado) + (dias * aluguel)

# 4 Pagamento

print(f"O valor total a pagar é de {preco:.2f}")
