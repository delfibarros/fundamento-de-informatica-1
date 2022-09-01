def eliminar(v,valor):
    i = 0
    while i < len(v):
        if v[i] == valor:
            del v[i]
            i -= 1
        i += 1

    return v

def listaNueva(v1,v2):
    largo2 = len(v2)
    for i in range(largo2):
        eliminar(v1,v2[i])
    
    return v1

lista = [9,6,10,2,2,15,3,4,5,11]
lista2 = [2,9,11]

nuevaLista = listaNueva(lista,lista2)
print(nuevaLista)


