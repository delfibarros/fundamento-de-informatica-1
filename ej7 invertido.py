numero = int(input("Numero: "))     
n = numero
invertido = 0

if numero < 0:
    numero = numero * -1

while numero != 0:                                         #123
    resto = numero % 10                                     #3 #2 #1
    invertido = (invertido * 10) + resto                    #3 #32 #321
    numero = numero // 10                                   #12 #1 #0
    
if n < 0:
    invertido = invertido * -1


print("Invertido: ", invertido) 