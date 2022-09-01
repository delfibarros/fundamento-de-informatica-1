def crearlista(x):
    lista = []
    numero = int(input("Ingresa un numero: "))
    while numero !=- 1:
        lista.append(numero)
        numero= int(input("Ingresa un numero: "))
    
    return lista


def busquedaSecuencial(lista1, buscarvalor):
    i = 0
    
    while i < len(lista1) and lista1[i] != buscarvalor:
        i += 1

    if i < len(lista1):
        return i
        
    else:
        return -1


def imprimirLista(v):
    largo = len(lista1)
    for i in range(largo):
        print(v[i],"", end= "")
    print("")


lista1 = crearlista(1)
buscarvalor = int(input("Ingrese el valor que desea buscar: "))

imprimirLista(lista1)

print(busquedaSecuencial(lista1, buscarvalor))

