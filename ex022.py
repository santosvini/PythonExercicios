nome = str(input("Digite seu nome: ")).strip()

print("String - Analisando Nome\n")

print(f"Seu nome completo em MAIUSCULO é: {nome.upper()}")
print(f"Seu nome completo em minúsculo é: {nome.lower()}")
print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(' ')))
print(f"Seu primeiro nome tem: {nome.find(' ')} letras")
