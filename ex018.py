print("Trigonometria\n")

from math import cos, sin, tan, radians

angulo = float(input("Qual o valor do ângulo? "))
seno = sin(radians(angulo))
print(f"O angulo é {angulo} e o valor do seno é {seno:.2f}\n")

#angulo = float(input("Qual o valor do ângulo? "))
cosseno = cos(radians(angulo))
print(f"O angulo é {angulo} e o valor do cosseno é {cosseno:.2f}\n")

#angulo = float(input("Qual o valor do ângulo? "))
tangente = tan(radians(angulo))
print(f"O valor do angulo é {angulo} e o valor da tangente é {tangente:.2f}\n")