print("#"*20)
print("Analisador Completo")
print("#"*20)

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""
totmulher20 = 0
for p in range(1, 5):
    print(f"--------- {p}º PESSOA --------")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f"A média de idade do grupo é de {mediaidade} anos!")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f"Ao todo são {totmulher20} mulher(es) com menos de 20 anos")