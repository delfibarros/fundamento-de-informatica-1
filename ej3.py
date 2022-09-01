numero = int(input("Ingrese numeros:"))
menor = numero
mayor = numero

while numero != -1:
    
    if numero > mayor:
        mayor = numero
    elif numero < menor:
       menor = numero

    numero = int(input("Ingrese numeros:"))

print("El menor es", menor)
print("El mayor es", mayor)
