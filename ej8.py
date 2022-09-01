import random

def numeros():
    vec = []
    
    numero = random.randint(0,100)
    menor = numero

    while numero != 0:
        vec.append(numero)
        numero = random.randint(0,100)
    
    largo = len(vec)

    print("El vector tiene",largo,"elementos.")

    for i in range(largo):
        if vec[i] < menor:
            menor = vec[i]

    print("El menor valor es el:",menor)

    posiciones = []

    for j in range(largo):
        if vec[j] == menor:
            posiciones.append(j)
    print("Se encuentra en las posiciones:",posiciones)
            

numeros()

