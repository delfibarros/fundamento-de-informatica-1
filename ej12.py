import random

def crearLista(n):
    vec = []
    for i in range(n):
        numero = random.randint(0,100)
        vec.append(numero)

    return vec

def imprimirLista(v):
    largo = len(v)
    for i in range(largo):
        print(v[i], end=" ")
    print("")


def ordenar(v):
    largo = len(v)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
    return v

def agregar(v,n):
    vec = []
    largo = len(v)
    aux = 0
    for i in range(largo):
        if n < v[i] and aux == 0:
            vec.append(n)
            aux = 1

        vec.append(v[i])
    
    if aux == 0:
        vec.append(n)

    return vec

elementos = int(input("Ingrese Cantidad de Elementos: "))

lista = crearLista(elementos)

print("Lista Desordenada:")
imprimirLista(lista)

listaOrdenada = ordenar(lista)
print("Lista Ordenada:")
imprimirLista(listaOrdenada)

N = int(input("Ingresar Numero: "))

listaConN = agregar(listaOrdenada, N)

print("Lista con N:",listaConN)

