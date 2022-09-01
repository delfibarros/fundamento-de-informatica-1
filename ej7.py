i = 1
suma = 0
numero = 0
mayor = 0
posicion = 10

while i <= 10:
    numero = int(input("Numero: ")) 
    suma = suma + numero

    if numero > mayor:
        mayor = numero
        posicion = i

    elif mayor > numero:
        mayor = mayor

    i = i + 1


print("Promedio", suma/10)
print("Mayor: ", mayor, "en la posicion: ", posicion)