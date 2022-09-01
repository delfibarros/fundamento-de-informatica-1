import random

#Forma 1 No permite agregar duplicados.

def metodoDeSeleccion(v): #Ordenar Lista
    largo = len(v)                    
    for i in range(largo-1):          
        for j in range(i+1,largo):    
            if v[i] > v[j]:             
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
    return v 

def busquedaSecuencial(v, dato):
    i = 0
    while i < len(v) and v[i] != dato:
        i += 1
    if i < len(v):
        return i
    else:
        return -1

def crearLista(elementos):
    vec = []
    
    for i in range(elementos):

        numero = random.randint(0,100)

        while busquedaSecuencial(vec, numero) != -1:
            numero = random.randint(0,100)
        
        vec.append(numero)

    return vec

cantidad = int(input("Cantidad de elementos: "))

lista = crearLista(cantidad)

print(lista)


            