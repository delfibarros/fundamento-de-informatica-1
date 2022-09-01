impar = 0
par = 0
numero = 0

while numero != -1:
    numero = int(input("Ingrese un numero del 0 al 9 o -1 para finalizar: "))
    if numero % 2 == 0:
        par += 1
    elif numero % 2 != 0:
        impar += 1

print("Par: ", par)    
print("Imar: ", impar - 1)