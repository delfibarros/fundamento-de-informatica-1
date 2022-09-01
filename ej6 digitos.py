numero = int(input("Numero: "))
numeroprint = numero
digitos = 0

while numero != 0:
    digitos += 1 
    if numero > 0:  
        numero = numero // 10
    if numero < 0:
        numero = numero // -10


print("El numero",numeroprint ,"tiene",digitos,"digitos.")

