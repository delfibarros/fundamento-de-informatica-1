n = 0
suma = 0
impares = 1

n = int(input("Numero Positivo: "))

while n < 0:
    n = int(input("Numero no Valido. Ingrese Numero Valido: "))


while impares <= n:
    suma = suma + impares
    print(impares)
    impares += 2

print("Suma: ", suma)