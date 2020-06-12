print("Cálculo da Hipotenusa")

from math import hypot

# Cateto oposto
co = float(input("Comprimento do cateto oposto: "))

# Cateto adjacente
ca = float(input("Comprimento do cateto adjacente: "))

# Cálculo da Hipotenusa
hp = hypot(ca, co)

# Comprimento da Hipotenusa
print(f"O Comprimento da hipotenusa é: {hp:.2f}")
