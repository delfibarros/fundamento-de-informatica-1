def valida(a, b):
    if a % b == 0:
        return True
    elif a % b != 0:
        return False

a = int(input("Numero 1: "))
b = int(input("Numero 2: "))

print(valida(a, b))