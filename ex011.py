largura = float(input("A largura é: "))
altura = float(input("A altura é: "))

parede = largura * altura
tinta = parede / 2

print(f"A sua parede tem a dimensão de {largura}x{altura} e sua área {largura * altura} m²")
print(f"Você precisa de {tinta:.2f}L de tinta para pintar a parede")
