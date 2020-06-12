print('=-'*17)
print("Confederação Nacional de Natação - CNN!")
print("=-"*17)

# Identificação do ano atual
from datetime import date
data_atual = date.today().year
# Inputação do ano de nascimento
ano_nascto = int(input("Digite seu ano de nascimento: "))
# Identificando idade
idade = data_atual - ano_nascto
# Condição
if idade <= 9:
    print(f"Você tem {idade} anos, está na categoria MIRIM!")
elif idade <= 14:
    print(f"Você tem {idade} anos, está na categoria INFANTIL!")
elif idade <= 19:
    print(f"Você tem {idade} anos, está na categoria JÚNIOR!")
elif idade <= 25:
    print(f"Você tem {idade} anos, está na categoria SÊNIOR!")
else:
    print(f"Você tem {idade} anos, está na categoria MASTER!")
