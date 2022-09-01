import random

def crearLista(n):
    vec = []
    for i in range(n):
        numero = random.randint(0,100)
        vec.append(numero)
    return vec

#Concatenar Valores Pares de A con Inpares de B
def c(v1,v2):
    v1Pares = []
    v2Impares = []
    

    largo1 = len(v1)
    largo2 = len(v2)

    for i in range(largo1):
        if (v1[i] % 2) == 0:
            v1Pares.append(v1[i])
    
    for i in range(largo2):
        if (v2[i] % 2) != 0:
            v2Impares.append(v2[i])

    largo = len(v2Impares)

    concatenacion = v1Pares

    for i in range(largo):
        numero = v2Impares[i]
        concatenacion.append(numero)
    
    return concatenacion

#D Valores impares de A con el reverso de los valres pares de B

def d(v1,v2):
    v1Impares = []
    v2Pares = []
    
    largo1 = len(v1)
    largo2 = len(v2)
    
    for i in range(largo1):
        if (v1[i] % 2) != 0:
            v1Impares.append(v1[i])

    for i in range(largo2):
        if (v2[i] % 2) == 0:
            v2Pares.append(v2[i])
    
    largov2Pares = len(v2Pares)

    for i in range(largov2Pares):
        invertido = 0
        numero = v2Pares[i]

        while numero != 0:                                      
            resto = numero % 10                                    
            invertido = (invertido * 10) + resto                    
            numero = numero // 10 
        
        v2Pares[i] = invertido

    largo = len(v2Pares)

    combinacion = v1Impares

    for i in range(largo):
        combinacion.append(v2Pares[i])

    return combinacion

#Intercalacion de A y B
def e(v1,v2):
    largo = len(v1)

    intercalacion = []

    for i in range(largo):
        intercalacion.append(v1[i])
        intercalacion.append(v2[i])

    return intercalacion


A = crearLista(5)
B = crearLista(5)
print("A:",A)
print("B:",B)
print("==============================================")
print("C (Pares del A con impares de B):", c(A,B))
print("==============================================")
print("D (Impares de A con reverso de pares de B)",d(A,B))
print("==============================================")
print("E (Intercalacion A y B):", e(A,B))
print("==============================================")