cantidad = int(input("Ingrese la cantidad de numeros que quiere: "))
i = 0
n1 = 0
n2 = 1

while i < cantidad:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    i += 1


