print("#"*18)
print("Menu de  Opções!")
print("#"*18)

from time import sleep
# Recebendo valores
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

# Menu de opções
opção = 0
while opção != 5:
    print("Aqui está seu menu de opções:\n"
          "[1] Somar\n"
          "[2] Multiplicar\n"
          "[3] Maior número\n"
          "[4] Novos Números\n"
          "[5] Sair\n")

    opção = int(input(">>>>> Digite a sua opção: "))
    if opção == 1:
        soma = valor1 + valor2
        print(f"O valor da soma entre {valor1} + {valor2} é {soma}!")
    elif opção == 2:
        multiplicacao = valor1 * valor2
        print(f"O valor da multiplicação entre {valor1} x {valor2} é {multiplicacao}!")
    elif opção == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
            print(f"O maior valor entre {valor1} e {valor2} é {maior}")
    elif opção == 4:
        print("Informe novos valores")
        valor1 = int(input("Digite valor: "))
        valor2 = int(input("Digite outro valor: "))
    elif opção == 5:
        print("Saindo.....\n")
    else:
        print("Opção Inválida. Tente Novamente!\n")
    print("=-="*10)
    sleep(1.5)
print("Volte Sempre!")