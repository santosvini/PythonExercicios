print("Reajuste de Salário!")

print("-" * 20)

salario = float(input("O seu salario é R$: "))
reajuste = (salario * 15 / 100)
novosal = salario + reajuste

print(f"O valor do aumento é de {reajuste:.2f}")
print(f"O valor do seu salário reajustado é {novosal:.2f}\n")

print("Parabéns vc foi reconhecico!")
