i = 0
suma = 0 

while suma <= 100:
    numero = int(input("Numero: "))
    i += 1
    if numero % 2 == 0:
        suma = suma + numero

print("Se ingresaron ", i, " numeros.")