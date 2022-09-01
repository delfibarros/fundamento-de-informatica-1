numero = int(input("Numero: "))
n = 0
divisor = numero

while divisor >= 1 and numero != 1 and numero != 0:
    if numero % divisor == 0: 
        n += 1
        divisor -= 1
    else:
        divisor -= 1

if n == 2:
    print("Primo")
elif numero == 1:
    print("Ni Primo Ni Compuesto")
elif numero == 0:
    print("Ni Primo Ni Compuesto") 
else:
    print("Compuesto")


