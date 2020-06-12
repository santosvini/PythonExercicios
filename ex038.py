print("*"*20)
print("Comparando Numeros")
print("*"*20)

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

if primeiro_valor > segundo_valor:
    print(f"O número {primeiro_valor} é MAIOR!")
elif segundo_valor > primeiro_valor:
    print(f"O número {segundo_valor} é MAIOR!")
else:
    print("Não existe valor MAIOR, os dois são IGUAIS!")
