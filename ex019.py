print("Sorteio de alunos\n")

from random import choice

#while True:
a1 = str(input("Digite o nome do primeiro aluno: "))
a2 = str(input("Digite o nome do segundo aluno: "))
a3 = str(input("Digite o nome do terceiro aluno: "))
a4 = str(input("Digite o nome do quarto aluno: "))
lista = [a1, a2, a3, a4]
aluno = choice(lista)
print(f"O aluno sorteado foi {choice(lista)}")
