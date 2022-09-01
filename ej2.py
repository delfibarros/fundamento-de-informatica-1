numero = int(input("Numero: "))
i = 0

while numero != -1:
    numero = int(input("Numero: "))
    i = i + 1

if i % 2 == 0:
    print("Es par.", i) 
else:
    print("Impar")