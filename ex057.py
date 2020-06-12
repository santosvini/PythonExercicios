print("#"*22)
print("Validador de Dados!")
print("#"*22)

# Lendo gênero da pessoa
sexo = str(input("Informe o sexo: [M/F]: ")).upper().strip()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")
