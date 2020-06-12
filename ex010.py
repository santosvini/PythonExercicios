real = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = real / 4.39
euro = real / 4.77
libra = real / 5.71
peso_arg = real / 0.07
boliv = real / 0.63
iene = real / 0.04

print("Você pode comprar {:.2f} Dolares".format(dolar))
print("Você pode comprar {:.2f} Euros".format(euro))
print("Você pode comprar {:.2f} Libras".format(libra))
print("Você pode comprar {:.2f} Peso Argentino".format(peso_arg))
print("Você pode comprar {:.2f} Peso Boliviano".format(boliv))
print("Você pode comprar {:.2f} Ienes".format(iene))
