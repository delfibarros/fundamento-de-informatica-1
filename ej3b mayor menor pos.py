numero = int(input("Ingrese numeros: "))

pos = 0
menor = numero
mayor = numero
posmayor = 1
posmenor = 1

while numero != -1:
    pos += 1
    if numero > mayor:
        mayor = numero
        posmayor = pos
    elif numero < menor:
       menor = numero
       posmenor = pos
    numero = int(input("Ingrese numeros: "))




print("El menor es", menor, "en la posicion:",posmenor)
print("El mayor es", mayor, "en la posicion:",posmayor)
