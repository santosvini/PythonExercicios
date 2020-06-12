print("+"*30)
print("Análise de Triângulos - v2.0!")
print("+"*30)

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("Os segmentos podem formar um triângulo", end='')
    if a == b == c:
        print(" Equilátero!")
    elif a != b != c != a:
        print(" Escaleno!")
    else:
        print(" Isósceles!")
else:
    print("Os segmentos não podem formar um triângulo ")