print("+++++++++++++++++++")
print("Grupo de Maioridade")
print("+++++++++++++++++++")

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pes in range(1, 8):
    ano = int(input(f"Em que ano a {pes}º pessoa nasceu?"))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f"Ao todo {totmaior} pessoas maiores de idade")
print(f"Ao todo {totmenor} pesoas menores de idade")
