print("===============")
print("MAIOR & MENOR")
print("===============")

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
c = int(input("Informe o terceiro número: "))

#Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o Maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado é {}".format(menor))
print("O maior valor digitado é {}".format(maior))
