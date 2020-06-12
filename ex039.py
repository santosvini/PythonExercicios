print("@"*30)
print("Alistamento - Serviço Militar")
print("@"*30)

from datetime import date

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f"Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}")

if idade == 18:
    print("É a hora de se alistar no serviço militar, IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Ainda falta {saldo} anos para o seu alistamento!")
    ano = ano_atual + saldo
    print(f"Seu alistamento será em {ano}")
else:
    idade > 18
    saldo = idade - 18
    print(f"Já passou {saldo} anos do tempo para o seu alistamento!")
    ano = ano_atual - saldo
    print(f"O seu alistamento foi em {ano}")