def crearLista(x):

    lista = []

    print("Lista",x,":")
    numero = int(input("Agregar Numero a la lista: "))
    while numero != -1:

        lista.append(numero)

        numero = int(input("Agregar Numero a la lista: "))
    
    return lista


def suma(y):
    largo = len(y)
    suma = 0
    for i in range(largo):
        suma += y[i]
    
    return suma

def imprimirLista(z):
    largo = len(z)
    for i in range(largo):
        print(z[i],"",end="")
    print("")




lista1 = crearLista(1)

imprimirLista(lista1)

suma = suma(lista1)

print("Suma: ", suma)






