def crearlista():
    vec = []
    numero = int(input("Numero: "))
    
    while numero != -1:
        vec.append(numero)
        numero = int(input("Numero: "))
    
    return vec

def ordenar(v):            
    largo = len(v)                    
    for i in range(largo-1):          
        for j in range(i+1,largo):    
            if v[i] > v[j]:             
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
    return v 

def busquedaBinaria(v, dato):
    largo = len(v)
    izquierda = 0
    derecha = largo-1
    pos = -1

    posiciones = []

    while izquierda <= derecha and pos == -1:
        centro = (izquierda + derecha) // 2
        if v[centro] == dato:
            pos = centro
        elif v[centro] < dato:
            izquierda = centro + 1
        else: 
            derecha = centro - 1

    return pos

#Busqueda binaria no busca 1 numero nomas?

lista = crearlista()
print(lista)

listaOrdenada = ordenar(lista)
print(listaOrdenada)

buscarValor = int(input("Valor: "))

posicion = busquedaBinaria(listaOrdenada, buscarValor)

print(posicion)