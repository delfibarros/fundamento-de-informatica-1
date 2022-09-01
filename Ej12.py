binario = int(input("Ingrese numero binario: "))

digito1 = (binario//10**3)%10
digito2 = (binario//10**2)%10
digito3 = (binario//10**1)%10
digito4 = (binario//10**0)%10

numero = digito1*(2**3)+digito2*(2**2)+digito3*(2**1)+digito4*(2**0)

print("El numero es: ", numero)

