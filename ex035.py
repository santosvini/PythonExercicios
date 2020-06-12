print("+"*30)
print("Análise de Triangulo - v1.0!")
print("+"*30)

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("É um triangulo!")
else:
    print("Não é um Triângulo!")