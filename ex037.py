print("-+"*10)
print("Conersor de Bases")
print("-+"*10)

num = int(input("Digite um número inteiro: "))
print("""Escolha uma das opções para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] CONVERTER PARA HEXADECIMAL""")
opção = int(input("Escolha sua opção: "))
if opção == 1:
    print(f"{num} convertido para BINÁRIO é igual a: {bin(num)[2:]}")
elif opção == 2:
    print(f"{num} convertido para OCTAL é igual a: {oct(num)[2:]}")
elif opção == 3:
    print(f"{num} convertido para HEXA é igual a: {hex(num)[2:]}")
else:
    print("Opção inválida, tente novamente!")