print("-"*20)
print("AUMENTO SALARIAL")
print("-"*20)

salario = float(input("Informe seu salario ao RH?:R$ "))

if salario > 1250.0:
    salario = salario + (salario*0.10)
    print(f"O seu salário foi reajustado para {salario:.2f} reais!")
else:
    salario <= 1250.0
    salario = salario + (salario*0.15)
    print(f"O seu salário foi reajustado para {salario:.2f} reais!")
print("Parabens pelo aumento!")