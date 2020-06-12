print("="*25)
print("Tratando Valores v1.0")
print("="*25)

num = cont = soma = 0
num = int(input("Informe um número [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Informe um número [999 para parar]: "))
print(f"Você digitou {cont} números e a soma deles é {soma}")
