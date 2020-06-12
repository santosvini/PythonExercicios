medida = float(input("Digite o valor da medida em metros: "))

km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print("A distancia em KM: {}".format(km))
print("A distancia em CM: {}".format(hm))
print("A distancia em DAM: {:.1f}".format(dam))
print("A distancia em DM: {}".format(dm))
print("A distancia em CM: {}".format(cm))
print("A distancia em MM: {}".format(mm))
