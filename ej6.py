def comparar(a, b):
    if a > b:
        return 1
    if a == b:
        return 0
    if a < b:
        return -1

numero1 = int(input("Numero1: "))
numero2 = int(input("Numero2: "))

print(comparar(numero1,numero2))