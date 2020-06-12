print("+="*12)
print("\033[4;31mEmpréstimo Bancário\033[m")
print("+="*12)

# Valor do imóvel
im = float(input("\033[1;30mQual o valor do imóvel? R$ \033[m"))
# Salário do comprador
sal = float(input("\033[1;30mQual é o seu salário? R$ \033[m"))
# Tempo de pagamento(Anos)
tempo = int(input("\033[1;30mQual o tempo pretendido para quitação? \033[m"))

prestacao = im / (tempo * 12)
minimo = sal * (30 / 100)
print(f"Para pagar uma casa de {im:.2f} em {tempo} anos", end="")
print(f"a prestação será de R${prestacao:.2f}")

if prestacao <= minimo:
    print("Empréstimo pode ser aprovado!")
else:
    print("O empréstimo não poderá ser aprovado")