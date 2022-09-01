numero = 0 

while numero <= 0:
    numero = int(input("Ingrese un numero: "))

x = 1
factorial = 1

while x <= numero:
    factorial = factorial * x
    x += 1

print("El facotrial de", numero,"es",factorial)
