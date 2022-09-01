def crearLista(x):

    lista = []

    print("Lista",x,":")
    numero = int(input("Agregar Numero a la lista: "))
    while numero != -1:

        lista.append(numero)

        numero = int(input("Agregar Numero a la lista: "))
    
    return lista

def busquedaSecuencial(lista1, buscarvalor):
    i = 0
    vec = []
    
    while i < len(lista1):
        if lista1[i] == buscarvalor:
            vec.append(i)
        i += 1

    if len(vec) > 0:
        return(vec)

    else:
        return -1

lista1 = crearLista(1)

buscarValor = int(input("Valor que desea buscar: "))


posicionesNumero = busquedaSecuencial(lista1,buscarValor)


print("El valor que buscabas esta en estas posiciones: ",posicionesNumero)
