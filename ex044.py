print("$"*26)
print("Gerenciador de pagamentos!")
print("$"*26, "\n")

# Verificando produto
preço = float(input("Informe o valor do produto: "))

# Escolha a forma de pagamento
print("Escolha melhor opção de pagamento!\n\n"
      "1. Dinheiro ou Cheque: 10% de desconto\n"
      "2. Á Vista com cartão: 5% de desconto\n"
      "3. Em 2x no cartão: Preço Normal\n"
      "4. 3x ou mais no cartão: 20% de juros\n")

opção = int(input("informe a opção de pagamento: "))
if opção == 1:
    pagamento = preço*(10/100)
    total = preço - pagamento
    print(f"O valor da compra é {preço} reais, com desconto de 10%, o preço total de {total:.2f} reais")
elif opção == 2:
    pagamento = preço*(5/100)
    total = preço - pagamento
    print(f"O valor da compra é {preço} reais, com desconto de 5%, o preço total de {total:.2f} reais")
elif opção == 3:
    pagamento = preço/2
    total = pagamento
    print(f"Sua compra parcelada em 2x de {total:.2f} reais")
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Quantas parcelas: "))
    parcela = total / totparc
    print(f"Sua compra será parcelada em {totparc}x , COM JUROS ")
    print(f"O valor da compra é {preço} reais, em 3x ou mais no cartão o valor é {total:.2f} reais")
else:
    total = preço
    print("Não existe essa opção de pagamento!")
print(f"Sua compra de {preço} sairá no valor de {total}")