print("#"*15)
print("Calculando IMC")
print("#"*15)

altura = float(input("Digite a sua altura (m): "))
peso = float(input("Digite o seu peso (Kg): "))
imc = peso / (altura**2)
print(f"O seu IMC é de: {imc:.2f}")

if imc < 18.5:
    print(f"Com o IMC de {imc:.1f}, você está: ABAIXO DO PESO!")
elif 18.5 <= imc < 25:
    print(f"Com o IMC de {imc:.1f}, você está no: PESO IDEAL!")
elif 25 <= imc < 30:
    print(f"Com o IMC de {imc:.1f}, você está no: SOBREPESO!, se exercite")
elif 30 <= imc < 40:
    print(f"Com o IMC {imc:.1f}, você está na: OBESIDADE!, se cuide!")
else:
    imc >= 40
    print(f"Com o IMC de {imc:.1f}, você está com: OBESIDADE MÓRBIDA!, cuidao")