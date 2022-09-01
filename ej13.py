
def crearLista():
    vec = []
    numero = int(input("Agregar Numero a la Lista: "))
    while numero != -1:
        vec.append(numero)
        numero = int(input("Agregar Numero a la Lista: "))

    return vec

def ordenar(v):
    largo = len(v)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if v[j] < v[i]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux

    return v

def intercalar(v1, v2):
    largo = len(v1)
    vec = []

    for i in range(largo):
        if v1[i] == v2[i]:
            vec.append(v1[i])
            vec.append(v2[i])
        if v1[i] > v2[i]:
            vec.append(v2[i])
            vec.append(v1[i])
        if v2[i] > v1[i]:
            vec.append(v1[i])
            vec.append(v2[i])

    return vec

#print("Lista M:")
#M = crearLista()
M = [99,50,60,10,7,9,2]

#print("Lista N:")
#N = crearLista()
N = [7,16,1,19,11,5,80]

print("Lista M:")
print("Desordenada:", M)
print("Ordenada:", ordenar(M))


print("Lista N:")
print("Desordenada:", N)
print("Ordenada:", ordenar(N))

intercalar = intercalar(ordenar(N), ordenar(M))

print("===========================")
print("N:",N)
print("M:",M)
print(intercalar)