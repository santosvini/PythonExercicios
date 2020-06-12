print("Apresentação de Alunos\n")

from random import shuffle

a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno: "))
a3 = str(input("Digite o nome do terceiro aluno: "))
a4 = str(input("Digite o nome do quato aluno: "))
lista = [a1, a2, a3, a4]
shuffle(lista)
sorted(lista)
print(f"Mostre a ordem de apresentação dos alunos {lista}\n")
