binario1 = int(input("Ingrese el primer digito del numero binario: "))
binario2 = int(input("Ingrese el segundo digito del numero binario: "))
binario3 = int(input("Ingrese el tercero digito del numero binario: "))
binario4 = int(input("Ingrese el cuarto digito del numero binario: "))

numero = binario1*(2**3) + binario2*(2**2) + binario3*(2**1) + binario4*(2**0)

print(binario1,binario2,binario3,binario4,"=",numero)