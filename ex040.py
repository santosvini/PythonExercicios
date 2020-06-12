print("%"*14)
print("Méddia Escolar")
print("%"*14)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota2+nota1) / 2
print(f"A sua média é {media:.1f} ")
if media < 5.0:
    print(f"Você foi REPROVADO sua média é de {media:.1f}, irá repetir o 3º colegial!")
elif 5.0 <= media <= 6.9:
    print(f"Você esta de RECUPERAÇÃO, pois a sua média é {media:.1f}, Estude!")
else:
    media >= 7.0
    print(f"Você foi APROVADO, sua média é {media:.1f}, Parábens, a faculdade te espera!")