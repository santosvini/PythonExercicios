print("+"*30)
print("Sequência de Fibonacci v1.0")
print("+"*30)

f = int(input("Quantos termos deseja mostrar? "))
ant = 0
pos = 1
print(f"{ant} → {pos} → ", end="")
cont = 3
while cont <= f:
    r = ant + pos
    print(f"{r} → ", end="")
    ant = pos
    pos = r
    cont += 1
print("FIM")