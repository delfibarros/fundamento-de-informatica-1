binario = int(input("Ingrese el numero binario: "))
binariostr = str(binario)

binario1 = int(binariostr[0])
binario2 = int(binariostr[1])
binario3 = int(binariostr[2])
binario4 = int(binariostr[3])

numero = binario1*(2**3) + binario2*(2**2) + binario3*(2**1) + binario4*(2**0)

print(int(numero))