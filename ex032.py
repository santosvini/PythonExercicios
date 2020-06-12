print("="*14)
print("ANO BISSEXTO!")
print("="*14)

from datetime import date
ano = int(input("Digite o ano para verificação: "))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano}, é ANO BISSEXTO!")
else:
    print(f"O ano de {ano}, não é ano BISSEXTO!")