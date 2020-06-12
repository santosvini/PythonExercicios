print("="*20)
print("Maior e Menor valores")
print("="*20)

maior = 0
menor = 0
soma = quant = media = 0

resp = "S"
while resp in "Ss":
    num = int(input("Digite um numero: "))
    soma += num
    quant += 1
    if num > maior:
        maior = num
    else:
        num < menor
        menor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / quant
print(f"Você digitou {quant} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")