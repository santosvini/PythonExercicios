print("Verificando Strings em Strings\n")

nome = (str(input("Qual o seu nome completo: "))).strip()
print(f"Seu nome tem Silva? {('Silva' in nome.lower())}")
